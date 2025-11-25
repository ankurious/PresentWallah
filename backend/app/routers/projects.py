from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import User, Project, Section, Revision, DocumentType
from app.schemas import (
    ProjectCreate, ProjectResponse, ProjectListResponse, ProjectUpdate,
    SectionResponse, SectionUpdate, GenerateContentRequest,
    RefineContentRequest, AISuggestRequest
)
from app.routers.auth import get_current_user
from app.services.llm import llm_service
from app.services.document import document_service

router = APIRouter(prefix="/api/projects", tags=["projects"])

@router.get("", response_model=List[ProjectListResponse])
def list_projects(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all projects for the current user"""
    projects = db.query(Project).filter(Project.user_id == current_user.id).order_by(Project.updated_at.desc()).all()
    return projects

@router.post("", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(
    project_data: ProjectCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new project with sections/slides"""
    # Create project
    doc_type = DocumentType.DOCX if project_data.document_type == "docx" else DocumentType.PPTX
    new_project = Project(
        title=project_data.title,
        document_type=doc_type,
        main_topic=project_data.main_topic,
        template=project_data.template if hasattr(project_data, 'template') and project_data.template else "modern",
        font_size=project_data.font_size if hasattr(project_data, 'font_size') and project_data.font_size else 20,
        user_id=current_user.id
    )
    db.add(new_project)
    db.flush()  # Get project ID
    
    # Create sections
    for section_data in project_data.sections:
        section = Section(
            project_id=new_project.id,
            title=section_data.title,
            order=section_data.order
        )
        db.add(section)
    
    db.commit()
    db.refresh(new_project)
    return new_project

@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(
    project_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get a specific project with all sections"""
    project = db.query(Project).filter(
        Project.id == project_id,
        Project.user_id == current_user.id
    ).first()
    
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    
    return project

@router.put("/{project_id}", response_model=ProjectResponse)
def update_project_settings(
    project_id: int,
    settings: ProjectUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update project settings (template, font_size)"""
    project = db.query(Project).filter(
        Project.id == project_id,
        Project.user_id == current_user.id
    ).first()
    
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    
    # Update settings
    if settings.template is not None:
        project.template = settings.template
    if settings.font_size is not None:
        project.font_size = settings.font_size
    
    db.commit()
    db.refresh(project)
    return project

@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(
    project_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete a project"""
    project = db.query(Project).filter(
        Project.id == project_id,
        Project.user_id == current_user.id
    ).first()
    
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    
    db.delete(project)
    db.commit()
    return None

@router.post("/generate-content", response_model=ProjectResponse)
def generate_content(
    request: GenerateContentRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Generate AI content for all sections in a project"""
    project = db.query(Project).filter(
        Project.id == request.project_id,
        Project.user_id == current_user.id
    ).first()
    
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    
    # Generate content for each section
    doc_type = "docx" if project.document_type == DocumentType.DOCX else "pptx"
    for section in project.sections:
        if not section.content:  # Only generate if empty
            content = llm_service.generate_content(
                section_title=section.title,
                main_topic=project.main_topic,
                document_type=doc_type
            )
            section.content = content
    
    db.commit()
    db.refresh(project)
    return project

@router.put("/sections/{section_id}", response_model=SectionResponse)
def update_section(
    section_id: int,
    section_update: SectionUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update section feedback (like/dislike, comment) or content"""
    section = db.query(Section).join(Project).filter(
        Section.id == section_id,
        Project.user_id == current_user.id
    ).first()
    
    if not section:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Section not found"
        )
    
    if section_update.content is not None:
        section.content = section_update.content
    if section_update.liked is not None:
        section.liked = section_update.liked
    if section_update.comment is not None:
        section.comment = section_update.comment
    
    db.commit()
    db.refresh(section)
    return section

@router.post("/refine-content", response_model=SectionResponse)
def refine_content(
    request: RefineContentRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Refine section content using AI"""
    section = db.query(Section).join(Project).filter(
        Section.id == request.section_id,
        Project.user_id == current_user.id
    ).first()
    
    if not section:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Section not found"
        )
    
    # Store revision history
    revision = Revision(
        section_id=section.id,
        prompt=request.prompt,
        previous_content=section.content,
        new_content=""  # Will be updated
    )
    
    # Get project to check document type
    project = section.project
    
    # Generate refined content
    refined_content = llm_service.refine_content(
        current_content=section.content,
        refinement_prompt=request.prompt,
        section_title=section.title,
        document_type=project.document_type.value
    )
    
    revision.new_content = refined_content
    section.content = refined_content
    
    db.add(revision)
    db.commit()
    db.refresh(section)
    return section

@router.post("/ai-suggest", response_model=List[str])
def ai_suggest_outline(
    request: AISuggestRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Generate AI-suggested outline/slide titles"""
    doc_type = "docx" if request.document_type == "docx" else "pptx"
    titles = llm_service.suggest_outline(
        main_topic=request.main_topic,
        document_type=doc_type,
        num_items=request.num_items
    )
    return titles

@router.get("/{project_id}/export")
def export_document(
    project_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Export project as .docx or .pptx file"""
    project = db.query(Project).filter(
        Project.id == project_id,
        Project.user_id == current_user.id
    ).first()
    
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    
    sections = db.query(Section).filter(Section.project_id == project_id).all()
    
    if project.document_type == DocumentType.DOCX:
        file_stream = document_service.generate_docx(project, sections)
        filename = f"{project.title}.docx"
        media_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    else:
        file_stream = document_service.generate_pptx(project, sections)
        filename = f"{project.title}.pptx"
        media_type = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    
    return StreamingResponse(
        file_stream,
        media_type=media_type,
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )

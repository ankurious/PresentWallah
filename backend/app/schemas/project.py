from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum

class DocumentTypeEnum(str, Enum):
    DOCX = "docx"
    PPTX = "pptx"

class SectionBase(BaseModel):
    title: str
    order: int

class SectionCreate(SectionBase):
    pass

class SectionUpdate(BaseModel):
    content: Optional[str] = None
    liked: Optional[bool] = None
    comment: Optional[str] = None

class SectionResponse(SectionBase):
    id: int
    content: str
    liked: Optional[bool] = None
    comment: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class ProjectBase(BaseModel):
    title: str
    document_type: DocumentTypeEnum
    main_topic: str
    template: Optional[str] = "modern"
    font_size: Optional[int] = 20

class ProjectCreate(ProjectBase):
    sections: List[SectionCreate]

class ProjectUpdate(BaseModel):
    template: Optional[str] = None
    font_size: Optional[int] = None

class ProjectResponse(ProjectBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    sections: List[SectionResponse] = []
    
    class Config:
        from_attributes = True

class ProjectListResponse(BaseModel):
    id: int
    title: str
    document_type: DocumentTypeEnum
    main_topic: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class GenerateContentRequest(BaseModel):
    project_id: int

class RefineContentRequest(BaseModel):
    section_id: int
    prompt: str

class AISuggestRequest(BaseModel):
    main_topic: str
    document_type: DocumentTypeEnum
    num_items: Optional[int] = None  # For pptx, number of slides

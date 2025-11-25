from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
import enum

class DocumentType(enum.Enum):
    DOCX = "docx"
    PPTX = "pptx"

class SlideTemplate(enum.Enum):
    MODERN = "modern"
    MINIMAL = "minimal"
    CORPORATE = "corporate"
    CREATIVE = "creative"

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    document_type = Column(Enum(DocumentType), nullable=False)
    main_topic = Column(Text, nullable=False)
    template = Column(String, default="modern")  # Slide template choice
    font_size = Column(Integer, default=20)  # Base font size for content
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    owner = relationship("User", back_populates="projects")
    sections = relationship("Section", back_populates="project", cascade="all, delete-orphan")

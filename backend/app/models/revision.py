from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Revision(Base):
    __tablename__ = "revisions"

    id = Column(Integer, primary_key=True, index=True)
    section_id = Column(Integer, ForeignKey("sections.id"), nullable=False)
    prompt = Column(Text, nullable=False)
    previous_content = Column(Text, nullable=False)
    new_content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    section = relationship("Section", back_populates="revisions")

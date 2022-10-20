from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from CRUD_TEST.project.core.models import Base

class Comment(Base):
    __tablename__ = "tbl_comment"

    detail = Column(String(300), nullable=False)

    user_id = Column(ForeignKey("user.id"), primary_key=True, index=True)
    content_id = Column(ForeignKey("content.id"), primary_key=True)

    user = relationship("User")
    content = relationship("Content")
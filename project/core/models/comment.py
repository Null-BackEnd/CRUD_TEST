from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from CRUD_TEST.project.core.models import Base

class Comment(Base):
    __tablename__ = "tbl_comment"

    content = Column(String(300), nullable=False)

    user_id = relationship("User", index=True)
    content_id = relationship("Content")
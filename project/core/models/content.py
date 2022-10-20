from sqlalchemy import Column, String, INT, ForeignKey
from sqlalchemy.orm import relationship
from CRUD_TEST.project.core.models import Base

class Content(Base):
    __tablename__ = "tbl_content"

    id = Column(INT, autoincrement=True, primary_key=True)
    detail = Column(String(3000), nullable=False)

    user_id = Column(ForeignKey("user.id"), primary_key=True)

    user = relationship("User")
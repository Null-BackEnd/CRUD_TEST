from sqlalchemy import Column, String, INT
from sqlalchemy.orm import relationship
from CRUD_TEST.project.core.models import Base

class Content(Base):
    __tablename__ = "tbl_content"

    id = Column(INT, autoincrement=True, primary_key=True)
    content = Column(String(3000), nullable=False)

    user_id = relationship("User")
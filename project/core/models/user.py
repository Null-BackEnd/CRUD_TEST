from sqlalchemy import INT, Column, String, CHAR
from project.core.models import Base

class User(Base):
    __tablename__ = "tbl_user"
    id = Column(INT, primary_key=True, autoincrement=True)
    account_id = Column(String(30), nullable=False)
    password = Column(String(60), nullable=False)
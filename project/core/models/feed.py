from sqlalchemy import Column, String, INT, ForeignKey
from sqlalchemy.orm import relationship, backref
from CRUD_TEST.project.core.models import Base

class Feed(Base):
    __tablename__ = "tbl_feed"

    id = Column(INT, autoincrement=True, primary_key=True)
    content = Column(String(3000), nullable=False)
    title = Column(String(100), nullable=False)
    user_id = Column(ForeignKey("tbl_user.id"), primary_key=True)

    user = relationship("User", backref=backref("writed_feeds"), foreign_keys=user_id)
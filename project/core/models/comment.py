from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from CRUD_TEST.project.core.models import Base

class Comment(Base):
    __tablename__ = "tbl_comment"

    content = Column(String(300), nullable=False)

    user_id = Column(ForeignKey("tbl_user.id"), primary_key=True, index=True)
    feed_id = Column(ForeignKey("tbl_feed.id"), primary_key=True)

    user = relationship("User", backref=backref("writed_comments"), foreign_keys=user_id)
    feed = relationship("Feed", backref=backref("feed_comments"), foreign_keys=feed_id)
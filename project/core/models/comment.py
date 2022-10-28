from sqlalchemy import Column, String, ForeignKey, INT
from sqlalchemy.orm import relationship, backref
from project.core.models import Base

class Comment(Base):
    __tablename__ = "tbl_comment"

    id = Column(INT, autoincrement=True, primary_key=True)
    content = Column(String(300), nullable=False)
    user_id = Column(ForeignKey("tbl_user.id"))
    feed_id = Column(ForeignKey("tbl_feed.id"))

    user = relationship("User", backref=backref("writed_comments"), foreign_keys=user_id)
    feed = relationship("Feed", backref=backref("feed_comments"), foreign_keys=feed_id)
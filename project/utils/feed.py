from project.core.models.feed import Feed
from project.core.models.user import User

from sqlalchemy.orm import Session
from project.utils.security import check_feed


def create_feed(title: str, content: str, user_id: int, session: Session):
    feed = Feed(
        title=title,
        content=content,
        user_id=user_id
    )

    session.add(feed)
    session.commit()

    return {
        "message": "success"
    }


def edit_feed(feed_id: int, title: str, content: str, user_id: int, session: Session):
    feed = check_feed(feed_id=feed_id, user_id=user_id, session=session)

    feed.title = title
    feed.content = content

    return {
        "message": "success"
    }


def delete_feed(feed_id: int, user_id: int, session: Session):
    feed = check_feed(feed_id=feed_id, user_id=user_id, session=session)

    session.delete(feed)

    return {
        "message": "success"
    }


def see_feed(feed_id: int, session: Session):
    feed = session.query(Feed).filter(Feed.id == feed_id).first()
    user = session.query(User).filter(User.id == feed.user_id).first()
    return {
        "post_id": feed.id,
        "username": user.account_id,
        "title": feed.title,
        "content": feed.content
    }
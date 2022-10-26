from project.core.models.comment import Comment
from project.core.models.user import User
from sqlalchemy.orm import Session


def is_my_comment(user_id=int, user=User):
    return True if user_id == user.id else False

def make_comment(user_id: int, content: str, session: Session):
    new_comment = Comment(
        content=content,
        user_id=user_id
    )

    session.add(new_comment)
    session.commit()

    return {
        "message": "success"
    }

def delete_comment(user_id: int, content: str, session: Session):
    is_my_comment(user_id)
    delete_comment = session.query(content)
    session.delete(delete_comment)
    session.commit()

def modify_comment(user_id: int, content: str, session: Session):
    is_my_comment(user_id)
    modify_comment = session.query(content).filter()
    modify_comment.update_one({content: content})

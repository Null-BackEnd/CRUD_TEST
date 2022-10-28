from project.core.models.comment import Comment
from sqlalchemy.orm import Session
from project.utils.security import check_comment


def write_comment(user_id: int, content: str,feed_id: int, session: Session):
    new_comment = Comment(
        content=content,
        feed_id=feed_id,
        user_id=user_id
    )

    session.add(new_comment)
    session.commit()

    return {
        "message": "success"
    }

def delete_comment(user_id: int, comment_id: int, session: Session):
    comment = check_comment(comment_id=comment_id, user_id=user_id, session=session)
    if comment:
        session.delete(comment)

    return {
        "message": "success"
    }

def modify_comment(user_id: int, content: str, comment_id: int , session: Session):
    comment = check_comment(comment_id=comment_id, user_id=user_id, session=session)
    if comment:
        comment.content = content

        return {
            "message": "success"
        }
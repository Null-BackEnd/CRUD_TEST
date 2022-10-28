from project.core.models.comment import Comment
from sqlalchemy.orm import Session
from project.utils.security import check_comment


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

def delete_comment(user_id: int, comment_id: int, session: Session):
    comment = check_comment(comment_id=comment_id, user_id=user_id, session=session)
    session.delete(comment)

    return {
        "message": "success"
    }

def modify_comment(user_id: int, content: str, comment_id: int , session: Session):
    comment = check_comment(comment_id=comment_id, user_id=user_id, session=session)
    if comment == True:
        modify_comment = session.query(content).filter()
        modify_comment.update_one({content: content})

        return {
            "message": "success"
        }
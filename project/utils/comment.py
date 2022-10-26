from project.core.models.comment import Comment

from sqlalchemy.orm import Session


def mk_comment(user_id: int, content: str, session: Session):
    new_comment = Comment(
        content=content,
        user_id=user_id
    )

    session.add(new_comment)
    session.commit()

    return {
        "message": "success"
    }

def del_comment(user_id: int, content: str, session: Session):
    del_commt = session.query(content)
    session.delete(del_commt)
    session.commit()

def mod_comment(user_id: int, content: str, session: Session):
    mod_commt = session.query(content)

    mod_commt.update_one({content: content})

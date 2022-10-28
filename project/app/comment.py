from project.core import session_scope
from project.utils.comment import write_comment
from project.utils.comment import modify_comment
from project.utils.comment import delete_comment
from project.core.schemas.comment import WriteComment
from project.core.schemas.comment import ModifyComment, DeleteComment
from project.core.models.user import User
from fastapi import APIRouter, status, Depends
from project.utils.security import get_current_user



app = APIRouter()


@app.post("")
async def writing_comment(body: WriteComment, user: User = Depends(get_current_user)):
    with session_scope() as session:
        request =  write_comment(content=body.content ,feed_id=body.feed_id, user_id=user.id, session=session)

        return request
@app.put("")
async def modifying_comment(body: ModifyComment, user: User = Depends(get_current_user)):
    with session_scope() as session:
        request = modify_comment(comment_id=body.comment_id, content=body.content, user_id=user.id, session=session)

        return request

@app.delete("")
async def deleting_comment(body: DeleteComment, user: User = Depends(get_current_user)):
    with session_scope() as session:
        requests = delete_comment(comment_id=body.comment_id, user_id=user.id, session=session)

        return requests
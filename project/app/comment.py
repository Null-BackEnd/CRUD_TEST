from project.core.models import session_scope
from project.core.schemas import comment
from project.utils.comment import make_comment
from project.utils.comment import modify_comment
from project.utils.comment import delete_comment

from fastapi import APIRouter

router = APIRouter()


@router.post("")
async def make_comment(body: comment.WriteComment):
    with session_scope() as session:
        request = make_comment(comment=body.comment_id,content=body.content ,post_id=body.feed_id, user_id=body.user_id, session=session)

        return request

@router.put("")
async def modify_comment(body: comment.ModifyComment):
    with session_scope() as session:
        request = modify_comment(comment=body.comment, content=body.content, user_id=body.user_id, session=session)

        return request

@router.delete("")
async def delete_comment(body: comment.WriteComment):
    with session_scope() as session:
        requests = delete_comment(comment_id=body.comment_id, user_id=body.user_id, session=session)

        return requests
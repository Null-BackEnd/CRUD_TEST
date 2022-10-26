from project.core.models import session_scope
from project.core.schemas import comment
from project.core.models.user import User
from project.core.models.feed import Feed
from project.utils.comment import make_comment
from project.utils.comment import modify_comment
from project.utils.comment import delete_comment

from fastapi import APIRouter

router = APIRouter()


@router.post("")
async def make_comment(body: comment, user=User, feed=Feed):
    with session_scope() as session:
        request = make_comment(comment=body.comment, post_id=feed.id, user_id=user.id, session=session)

        return request

@router.put("")
async def modify_comment(body: comment, user=User, feed=Feed):
    with session_scope() as session:
        request = modify_comment(comment=body.comment, post_id=feed.id, user_id=user.id, session=session)

        return request

@router.delete("")
async def delete_comment(body: comment, feed=Feed, user=User):
    with session_scope() as session:
        requests = delete_comment(comment=body.comment, feed=feed.id, user_id=user.id, session=session)

        return requests
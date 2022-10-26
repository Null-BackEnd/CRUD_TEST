from project.core.models import session_scope
from project.core.schemas import comment
from project.core.models.user import User
from project.utils.comment import mk_comment
from project.utils.comment import mod_comment
from project.utils.comment import del_comment

from fastapi import APIRouter

router = APIRouter()


@router.post("")
async def mk_comment(body: comment, user=User):
    with session_scope() as session:
        request = mk_comment(comment=body.comment, user_id=user.id, session=session)

        return request

@router.put("")
async def mod_comment(body: comment, user=User):
    with session_scope() as session:
        request = mod_comment(comment=body.comment, user_id=user.id, session=session)

        return request

@router.delete("")
async def del_comm(body: comment, user=User):
    with session_scope() as session:
        requests = del_comment(comment=body.comment, user_id=user.id, session=session)

        return requests


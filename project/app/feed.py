from project.core import session_scope
from project.core.models.user import User
from project.core.schemas.feed import Feed
from project.utils.feed import create_feed, edit_feed, delete_feed, see_feed
from fastapi import APIRouter, status, Depends
from project.utils.security import get_current_user

app = APIRouter()

@app.post("/", status_code=status.HTTP_201_CREATED)
async def write_feed(body: Feed, user: User = Depends(get_current_user)):
    with session_scope() as session:
        req = create_feed(title=body.title, content=body.content, user_id=user.id, session=session)
        return req

@app.put("/{feed_id}")
async def update_feed(feed_id: int, body: Feed, user: User = Depends(get_current_user)):
    with session_scope() as session:
        req = edit_feed(feed_id=feed_id, title=body.title, content=body.content, user_id=user.id, session=session)
        return req

@app.delete("/{feed_id}")
async def remove_feed(feed_id: int, user: User = Depends(get_current_user)):
    with session_scope() as session:
        req = delete_feed(session=session, feed_id=feed_id, user_id=user.id)
        return req

@app.get("/{feed_id}")
async def get_feed(feed_id: int):
    with session_scope() as session:
        req = see_feed(feed_id=feed_id, session=session)
        return req

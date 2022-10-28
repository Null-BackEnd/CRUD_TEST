from fastapi import APIRouter

from project.app import auth, comment, feed

api_router = APIRouter()

api_router.include_router(auth.app, prefix="/auths", tags=["auth"])
api_router.include_router(feed.app, prefix="/feeds", tags=["feed"])
api_router.include_router(comment.app, prefix="/comments", tags=["comment"])
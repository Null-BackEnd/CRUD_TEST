from fastapi import APIRouter

from CRUD_TEST.project.app import auth, comment, feed

api_router = APIRouter()

api_router.include_router(auth.app, prefix="/auths", tags=["auth"])
api_router.include_router(feed.app, prefix="/feeds", tags=["feed"])
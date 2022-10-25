from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from CRUD_TEST.project.core.models.user import User

from CRUD_TEST.project.utils.security import get_password_hash, verify_password, create_access_token

def create_user(session: Session, account_id: str, password: str):
    session.add(
        User(
            account_id=account_id,
            password=get_password_hash(password)
        )
    )
    return HTTPException(status_code=status.HTTP_201_CREATED, detail="success")

def login(session: Session, account_id: str, password: str):
    user = session.query(User.id, User.account_id, User.password).filter(User.account_id == account_id)
    if not user.scalar():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id does not exist")
    user = user.first()
    if not verify_password(plain_password=password, hashed_password=user["password"]):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Wrong password")

    return {
        "access_token": create_access_token(id=user["id"])
    }

def check_id(session: Session, user_id: str):
    user = session.query(User.account_id).filter(User.id == user_id)

    if user.scalar():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Overlap")

    else:
        return {
            "message": "Available"
        }
from passlib.context import CryptContext
from fastapi import HTTPException, Depends, status

from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from CRUD_TEST.project.core.config import ACCESS_TIMEOUT, SECRET, ALGORITHM
from CRUD_TEST.project.core import session_scope
from CRUD_TEST.project.core.models.user import User
from CRUD_TEST.project.core.models.feed import Feed

from sqlalchemy.orm import Session
import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(id: str):
    exp = datetime.utcnow() + timedelta(minutes=ACCESS_TIMEOUT)
    encoded_jwt = jwt.encode({"exp": exp, "sub": id}, SECRET, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    with session_scope() as session:
        a = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Colud not validate credentials"
        )
        try:
            payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
            id: str = payload.get("sub")
            if id is None:
                raise credentials_exception
        except:
            raise credentials_exception
        user = session.query(User).filter(User.id == id)
        if not user.scalar():
            raise credentials_exception
        return user.first()

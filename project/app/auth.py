from CRUD_TEST.project.core.schemas.user import SignUp, Login
from CRUD_TEST.project.core import session_scope
from CRUD_TEST.project.utils.auth import create_user, login, check_id

from fastapi import APIRouter, HTTPException, status

app = APIRouter()

@app.post("/check")
async def checking_id(user_id: str):
    with session_scope() as session:
        return check_id(user_id=user_id, session=session)

@app.post("/signup")
async def sign_up(body: SignUp):
    if not(body.account_id and body.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="check id or password")
    with session_scope() as session:
        return create_user(account_id=body.account_id, password=body.password, session=session)

@app.post("/login")
async def logins(body: Login):
    with session_scope() as session:
        return login(account_id=body.account_id, password=body.password, session=session)
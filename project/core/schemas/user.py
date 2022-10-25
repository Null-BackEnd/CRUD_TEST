from pydantic import BaseModel, constr

class SignUp(BaseModel):
    account_id: constr(min_length=1, max_length=30)
    password: str

class Login(BaseModel):
    account_id: constr(min_length=1, max_length=30)
    password: str
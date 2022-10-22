from pydantic import BaseModel, constr

class Writing(BaseModel):
    title: constr(min_length=1, max_length=100)
    detail: constr(min_length=1, max_length=3000)
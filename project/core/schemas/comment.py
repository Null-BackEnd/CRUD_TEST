from pydantic import BaseModel, constr

class WriteComment(BaseModel):
    id: int
    content: constr(min_length=1, max_length=300)

class ModifyComment(BaseModel):
    id: int
    content: constr(min_length=1, max_length=300)
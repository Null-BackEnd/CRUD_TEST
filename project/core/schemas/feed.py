from pydantic import BaseModel, constr

class WriteFeed(BaseModel):
    title: constr(min_length=1, max_length=100)
    content: constr(min_length=1, max_length=3000)

class ModifyFeed(BaseModel):
    id: int
    title: constr(min_length=1, max_length=100)
    content: constr(min_length=1, max_length=3000)
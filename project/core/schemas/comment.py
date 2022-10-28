from pydantic import BaseModel, constr

class WriteComment(BaseModel):
    feed_id: int
    content: constr(min_length=1, max_length=300)

class ModifyComment(BaseModel):
    comment_id: int
    content: constr(min_length=1, max_length=300)

class DeleteComment(BaseModel):
    comment_id: int

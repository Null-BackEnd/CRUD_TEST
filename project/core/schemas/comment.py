from pydantic import BaseModel, constr

class Comment(BaseModel):
    datail: constr(min_length=1, max_length=300)
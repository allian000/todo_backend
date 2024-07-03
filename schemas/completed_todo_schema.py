from pydantic import BaseModel

class CompletedTodoCreate(BaseModel):
    title: str
    content: str
    is_checked: bool

class CompletedTodoRead(BaseModel):
    id: int
    title: str
    content: str
    is_checked: bool
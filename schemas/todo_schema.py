from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    content: str
    is_checked: bool

class TodoRead(BaseModel):
    id: int
    title: str
    content: str
    is_checked: bool
    
class TodoUpdate(BaseModel):
    title: str
    content: str
    is_checked: bool
    
class TodoUpdateCheckStatus(BaseModel):
    is_checked: bool
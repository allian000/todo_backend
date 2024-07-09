from typing import List
from sqlalchemy.orm import Session

from models import completed_todo_model as TodoCompleteModel
import schemas.completed_todo_schema as TodoCompleteSchema
import schemas.todo_schema as TodoSchema

def get_todo_completeds(db: Session):
    return db.query(TodoCompleteModel.CompletedTodo).all()

def create_todo_completeds(db: Session, todoList: List[TodoSchema.TodoRead], todoCompleteIdList: List[int]):
    db_todoCompleteItemList = []
    for item in todoList:
        if item.id in todoCompleteIdList:
            db_todoCompleteItemList.append(TodoCompleteModel.CompletedTodo(title=item.title, content=item.content, is_checked=item.is_checked))
    db.add_all(db_todoCompleteItemList)
    db.commit()

    return db_todoCompleteItemList
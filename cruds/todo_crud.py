from typing import List
from sqlalchemy.orm import Session

from models import todo_model as TodoModel
import schemas.todo_schema as TodoSchema

def get_todos(db: Session):
    return db.query(TodoModel.Todo).all()

def create_todo(db: Session, todo: TodoSchema.TodoCreate):
    db_todo = TodoModel.Todo(title=todo.title, content=todo.content)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session,itemId:int, todoItem: TodoSchema.TodoUpdate):
    db_item = db.query(TodoModel.Todo).filter(TodoModel.Todo.id == itemId).first()
    db_item.title = todoItem.title
    db_item.content = todoItem.content
    db_item.is_checked = todoItem.is_checked
    db.commit()
    return db_item

def update_todo_check_status(db: Session,itemId:int, todoItem: TodoSchema.TodoUpdateCheckStatus):
    db_item = db.query(TodoModel.Todo).filter(TodoModel.Todo.id == itemId).first()
    db_item.is_checked = todoItem.is_checked
    db.commit()
    return db_item

def delete_todo(db: Session, todoId: int):
    db_item = db.query(TodoModel.Todo).filter(TodoModel.Todo.id == todoId).first()
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully"}

def delete_todo_with_list(db: Session, todoIdList: List[int]):
    db_items = db.query(TodoModel.Todo).all()
    for item in db_items:
        if item.id in todoIdList:
            db.delete(item)
    db.commit()
    return {"message": "Items deleted successfully"}
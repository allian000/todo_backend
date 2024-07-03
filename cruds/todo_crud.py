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
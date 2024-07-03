from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
import schemas.todo_schema as schemas
import cruds.todo_crud as crud

router = APIRouter()

@router.get("/", response_model=List[schemas.TodoRead])
def getTodoList(db:Session = Depends(get_db)):
    return crud.get_todos(db)

@router.post("/", response_model=schemas.TodoRead)
def createTodo(todo:schemas.TodoCreate, db:Session = Depends(get_db)):
    return crud.create_todo(db, todo)
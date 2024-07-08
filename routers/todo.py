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

@router.put("/updateTodo/{todo_id}", response_model=schemas.TodoUpdate)
def updateTodo(todo_id: int, todoItem:schemas.TodoUpdate, db:Session = Depends(get_db)):
    return crud.update_todo(itemId=todo_id, db=db, todoItem=todoItem)

@router.put("/updateTodoCheckStatu/{todo_id}", response_model=schemas.TodoUpdateCheckStatus)
def updateTodo(todo_id: int, todoItem:schemas.TodoUpdateCheckStatus, db:Session = Depends(get_db)):
    return crud.update_todo_check_status(itemId=todo_id, db=db, todoItem=todoItem)

@router.delete("/deleteTodo/{todo_id}")
def updateTodo(todo_id: int, db:Session = Depends(get_db)):
    return crud.delete_todo(itemId=todo_id, db=db)
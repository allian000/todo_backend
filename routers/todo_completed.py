from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
import schemas.completed_todo_schema as schemas
import cruds.todo_completed_crud as crud
from routers import todo as todoRouter

router = APIRouter()

@router.get("/", response_model=List[schemas.CompletedTodoRead])
def getTodoCompleteList(db:Session = Depends(get_db)):
    return crud.get_todo_completeds(db)

@router.post("/", response_model=List[schemas.CompletedTodoRead])
def createTodoCompletes(todoIdItems:List[int], db:Session = Depends(get_db)):
    # return crud.create_todo(db, todo)
    todoList = todoRouter.getTodoList(db=db)
    add_status = crud.create_todo_completeds(db=db,todoList=todoList, todoCompleteIdList=todoIdItems)
    del_status = todoRouter.deleteTodoWithList(db=db, todoIdList=todoIdItems)
    return add_status
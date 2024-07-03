from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from routers import todo
from models import todo_model

todo_model.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = [
    "http://localhost",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Message":"Hello World!"}

app.include_router(todo.router,prefix="/todo", tags=["todo"])
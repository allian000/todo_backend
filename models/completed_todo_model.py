from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base


class CompletedTodo(Base):
    __tablename__ = "completed_todos"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
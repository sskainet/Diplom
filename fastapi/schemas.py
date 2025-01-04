from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: str
    priority: int
    due_date: date
    user_id: int


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    pass


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    categories: List[CategoryBase] = []

    class Config:
        orm_mode = True

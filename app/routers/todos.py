from typing import List
from uuid import uuid4
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Todo, User
from app.schemas import TodoCreate, TodoUpdate, TodoResponse
from app.auth import get_current_user

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(
    todo_data: TodoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    new_todo = Todo(
        id=str(uuid4()),
        description=todo_data.description,
        scheduled_at=todo_data.scheduled_at,
        status=todo_data.status,
        owner_id=current_user.id,
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@router.get("/", response_model=List[TodoResponse])
def get_todos(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return db.query(Todo).filter(Todo.owner_id == current_user.id).all()


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(
    todo_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    todo = (
        db.query(Todo)
        .filter(Todo.id == todo_id, Todo.owner_id == current_user.id)
        .first()
    )
    if not todo:
        raise HTTPException(status_code=404, detail="Task not found")
    return todo


@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: str,
    todo_update: TodoUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    todo = (
        db.query(Todo)
        .filter(Todo.id == todo_id, Todo.owner_id == current_user.id)
        .first()
    )
    if not todo:
        raise HTTPException(status_code=404, detail="Task not found")

    if todo_update.description is not None:
        todo.description = todo_update.description
    if todo_update.scheduled_at is not None:
        todo.scheduled_at = todo_update.scheduled_at
    if todo_update.status is not None:
        todo.status = todo_update.status

    db.commit()
    db.refresh(todo)
    return todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(
    todo_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    todo = (
        db.query(Todo)
        .filter(Todo.id == todo_id, Todo.owner_id == current_user.id)
        .first()
    )
    if not todo:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(todo)
    db.commit()
    return None
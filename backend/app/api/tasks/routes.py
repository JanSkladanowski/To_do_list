from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.models.tasks import Task
from app.schemas.tasks import TaskCreate, TaskResponse
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TaskResponse)
async def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/{task_id}", response_model=TaskResponse)
async def get_single_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.TaskID == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found.")
    return db_task

@router.put("/{task_id}", response_model=TaskResponse)
async def modify_task(task_id: int, task_update: TaskCreate, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.TaskID == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found.")
    for key, value in task_update.model_dump().items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.delete("/{task_id}", response_model=TaskResponse)
async def remove_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.TaskID == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found.")
    db.delete(db_task)
    db.commit()
    return db_task

from pydantic import BaseModel, Field
from datetime import date

class TaskCreate(BaseModel):
    TaskName: str
    Description: str
    Deadline: date
    Completed: bool = False

class TaskResponse(TaskCreate):
    TaskID: int

    class Config:
        json_encoders = {
            date: lambda v: v.strftime("%Y-%m-%d"),
        }

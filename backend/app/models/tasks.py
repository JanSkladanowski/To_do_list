from sqlalchemy import Column, Integer, String, Boolean, Date
from app.core.database import Base

class Task(Base):
    __tablename__ = 'tasks'

    TaskID = Column(Integer, primary_key=True, index=True)
    TaskName = Column(String)
    Description = Column(String)
    Deadline = Column(Date)
    Completed = Column(Boolean)

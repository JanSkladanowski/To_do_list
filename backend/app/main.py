from fastapi import FastAPI
from app.api.tasks import routes as task_routes
from decouple import config


app = FastAPI()

DATABASE_URL = config('SQLALCHEMY_DATABASE_URL')

app.include_router(task_routes.router, prefix="/api/tasks")

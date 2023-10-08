import factory
from datetime import datetime, timedelta
from app.schemas.tasks import TaskCreate

class BaseTaskFactory(factory.Factory):
    class Meta:
        model = TaskCreate
    
    TaskName = factory.Faker('sentence', nb_words=3)
    Description = factory.Faker('paragraph')
    Deadline = factory.LazyFunction(lambda: (datetime.utcnow() + timedelta(days=1)).strftime("%Y-%m-%d"))
    Completed = False
    print(Deadline)

class UrgentTaskFactory(BaseTaskFactory):
    Deadline = factory.LazyFunction(lambda: (datetime.utcnow() + timedelta(days=1)).strftime("%Y-%m-%d"))


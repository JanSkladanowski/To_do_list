from tests.tasksFactory import BaseTaskFactory, UrgentTaskFactory

def test_create_task(client, db_session):
    # Given
    task_to_create = BaseTaskFactory()
    task_data = task_to_create.dict()
    task_data['Deadline'] = task_data['Deadline'].strftime("%Y-%m-%d")  # Konwersja daty na string

    # When
    response = client.post("/api/tasks/", json=task_data)

    # Then
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["TaskName"] == task_to_create.TaskName
    assert data["Description"] == task_to_create.Description
    assert "TaskID" in data

def test_get_task(client, db_session):
    # Given
    task_to_create = UrgentTaskFactory()
    # Assume a task with ID 1 exists, either create it here or 
    # use an existing one if your test DB is not empty
    
    # When
    response = client.get("/api/tasks/1")

    # Then
    assert response.status_code == 200, response.text
    data = response.json()
    # Note: Without creating the exact task in DB, these assertions might fail
    # Ideally, you'd create a task first (using POST), and then GET it using its ID
    assert data["TaskName"] == "Test Task"
    assert data["Description"] == "Test Description"
    assert "TaskID" in data
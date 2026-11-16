from app.tasks import tasks, next_task_id
from app.models import Task
from fastapi import HTTPException


@app.get("/")
def home():
    return {
        "message": "Welcome to Task Management API",
        "status": "running"
    }

from app.tasks import tasks

@app.get("/tasks")
def get_all_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: Task):
    global next_task_id


    new_task = task.model_copy(
        update={"id": next_task_id}
    )


    tasks.append(new_task.model_dump())
    next_task_id += 1


    return new_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)

            return {
                "message": "Task deleted successfully",
                "deleted_task": task
            }

    return {
        "message": "Task not found"
    }
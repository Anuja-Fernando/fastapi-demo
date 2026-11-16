from fastapi import FastAPI, HTTPException
from app.tasks import tasks, next_task_id
from app.models import Task

app = FastAPI(
    title="Task Management API",
    description="A simple API to manage daily tasks",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Task Management API",
        "status": "running"
    }


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


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):

    for index, task in enumerate(tasks):

        if task["id"] == task_id:

            updated_data = updated_task.model_copy(
                update={"id": task_id}
            )

            tasks[index] = updated_data.model_dump()

            return tasks[index]

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
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

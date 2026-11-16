from fastapi import FastAPI

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

from app.tasks import tasks

@app.get("/tasks")
def get_all_tasks():
    return tasks

"""update-task"""git 

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
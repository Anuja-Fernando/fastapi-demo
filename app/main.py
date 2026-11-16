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
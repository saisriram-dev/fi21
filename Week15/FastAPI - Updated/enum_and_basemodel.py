from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# 1. Define the Enum for strict priority choices
class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


# 2. Define the Pydantic BaseModel using the Enum
class Task(BaseModel):
    id: int
    title: str
    description: str
    priority: Priority  # Accepts ONLY "low", "medium", or "high"


# ENDPOINT 1: Create a task (Tests JSON Body Validation)
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    # If the user passes an invalid priority (e.g. "urgent"),
    # FastAPI automatically rejects it with a 422 Error before hitting this line.
    return task


# ENDPOINT 2: Filter tasks (Tests URL Query Parameter Validation)
@app.get("/tasks/")
def list_tasks(priority: Priority):
    # Forces the client to choose ?priority=low, medium, or high
    return {"message": f"Fetching tasks with priority: {priority.value}"}


# ENDPOINT 3: Get a specific task by ID
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    return Task(
        id=task_id,
        title="Example Task",
        description="This is an example task.",
        priority=Priority.MEDIUM,
    )

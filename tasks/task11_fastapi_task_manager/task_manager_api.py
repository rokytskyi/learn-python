# Task 11: Task Manager API with FastAPI
# This is a starter file for the Task Manager API
# Complete the code to implement all the required features

from fastapi import FastAPI, HTTPException, Depends, Query, Path, status
from pydantic import BaseModel, Field
from typing import List, Optional
import json
from datetime import datetime
from enum import Enum

# Define Pydantic models for request and response validation
class PriorityEnum(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class TaskBase(BaseModel):
    """Base model for task data."""
    title: str
    description: str
    due_date: str
    priority: PriorityEnum

class TaskCreate(TaskBase):
    """Model for creating a new task."""
    pass

class TaskUpdate(BaseModel):
    """Model for updating a task."""
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[str] = None
    priority: Optional[PriorityEnum] = None

class Task(TaskBase):
    """Model for a task with ID and completion status."""
    id: int
    completed: bool = False

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Complete Python Project",
                "description": "Finish the FastAPI task manager project",
                "due_date": "2025-09-01",
                "priority": "high",
                "completed": False
            }
        }

# Task Manager class for data persistence
class TaskManager:
    """Class for managing tasks with file persistence."""
    
    def __init__(self, filename: str = "tasks.json"):
        """Initialize the task manager with the given filename."""
        self.filename = filename
        self.tasks = []
        self.load_tasks()
        
    # Implement the following methods:
    # - get_tasks()
    # - get_task(task_id)
    # - add_task(task)
    # - update_task(task_id, task_update)
    # - delete_task(task_id)
    # - mark_task_complete(task_id)
    # - filter_tasks(status, priority)
    # - save_tasks()
    # - load_tasks()

# Create FastAPI application
app = FastAPI(
    title="Task Manager API",
    description="A simple API for managing tasks",
    version="1.0.0"
)

# Dependency to get TaskManager instance
def get_task_manager():
    """Dependency for getting the TaskManager instance."""
    return TaskManager()

# API Endpoints

@app.get("/")
async def root():
    """Root endpoint that returns a welcome message."""
    return {"message": "Welcome to the Task Manager API"}

@app.get("/tasks", response_model=List[Task], status_code=status.HTTP_200_OK)
async def get_tasks(
    task_manager: TaskManager = Depends(get_task_manager)
):
    """Get all tasks."""
    # Your code here:
    pass

@app.get("/tasks/{task_id}", response_model=Task, status_code=status.HTTP_200_OK)
async def get_task(
    task_id: int = Path(..., title="The ID of the task to get", ge=1),
    task_manager: TaskManager = Depends(get_task_manager)
):
    """Get a specific task by ID."""
    # Your code here:
    pass

@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(
    task: TaskCreate,
    task_manager: TaskManager = Depends(get_task_manager)
):
    """Create a new task."""
    # Your code here:
    pass

@app.put("/tasks/{task_id}", response_model=Task, status_code=status.HTTP_200_OK)
async def update_task(
    task_id: int = Path(..., title="The ID of the task to update", ge=1),
    task_update: TaskUpdate = ...,
    task_manager: TaskManager = Depends(get_task_manager)
):
    """Update a task."""
    # Your code here:
    pass

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int = Path(..., title="The ID of the task to delete", ge=1),
    task_manager: TaskManager = Depends(get_task_manager)
):
    """Delete a task."""
    # Your code here:
    pass

@app.patch("/tasks/{task_id}/complete", response_model=Task, status_code=status.HTTP_200_OK)
async def mark_task_complete(
    task_id: int = Path(..., title="The ID of the task to mark as complete", ge=1),
    task_manager: TaskManager = Depends(get_task_manager)
):
    """Mark a task as complete."""
    # Your code here:
    pass

@app.get("/tasks/filter", response_model=List[Task], status_code=status.HTTP_200_OK)
async def filter_tasks(
    completed: Optional[bool] = Query(None, title="Filter by completion status"),
    priority: Optional[PriorityEnum] = Query(None, title="Filter by priority"),
    task_manager: TaskManager = Depends(get_task_manager)
):
    """Filter tasks by status or priority."""
    # Your code here:
    pass

# Run the application with: uvicorn task_manager_api:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("task_manager_api:app", host="127.0.0.1", port=8000, reload=True)
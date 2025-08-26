# Task 11: Task Manager API with FastAPI

## Objective
Transform the Task Manager from Task 10 into a web API using FastAPI, introducing web development concepts and RESTful API design.

## Instructions
Create a RESTful API for the Task Manager with the following features:
1. Set up a FastAPI application
2. Implement API endpoints for:
   - Creating tasks
   - Retrieving all tasks
   - Retrieving a specific task by ID
   - Updating a task
   - Marking a task as complete
   - Deleting a task
   - Filtering tasks by status or priority
3. Use proper HTTP methods (GET, POST, PUT, DELETE)
4. Implement request validation using Pydantic models
5. Add error handling and appropriate HTTP status codes
6. Document your API with automatic Swagger/OpenAPI documentation
7. Implement data persistence (can use the same JSON file approach as Task 10)

## Concepts to Apply
- FastAPI framework
- RESTful API design principles
- HTTP methods and status codes
- Request and response models with Pydantic
- Path and query parameters
- Dependency injection
- API documentation
- Error handling in web applications
- Asynchronous programming (optional)

## Expected Output
A running FastAPI application that:
- Provides all the functionality of the Task Manager from Task 10
- Uses appropriate HTTP methods for different operations
- Returns proper status codes and error messages
- Has automatic API documentation via Swagger UI
- Validates request data using Pydantic models
- Persists task data between application restarts

## API Endpoints to Implement

```
GET /tasks - Get all tasks
GET /tasks/{task_id} - Get a specific task
POST /tasks - Create a new task
PUT /tasks/{task_id} - Update a task
DELETE /tasks/{task_id} - Delete a task
PATCH /tasks/{task_id}/complete - Mark a task as complete
GET /tasks/filter - Filter tasks by status or priority
```

## Tips
- Crate & activate python virtual environment 
  - `python3 -m venv env`
  - `source env/bin/activate`
- Install FastAPI and Uvicorn: `pip install fastapi uvicorn`
- You can reuse the Task class from Task 10, converting it to a Pydantic model
- Use FastAPI's automatic documentation at `/docs` to test your API
- HTTP status codes to consider:
  - 200: OK (successful GET, PUT, PATCH)
  - 201: Created (successful POST)
  - 204: No Content (successful DELETE)
  - 400: Bad Request (invalid input)
  - 404: Not Found (resource doesn't exist)
  - 422: Unprocessable Entity (validation error)
- Use FastAPI's dependency injection for the TaskManager
- Consider using async/await for better performance (optional)
- Test your API with tools like curl, Postman, or the built-in Swagger UI
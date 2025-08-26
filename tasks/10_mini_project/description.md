# Task 10: Mini Project - Task Manager

## Objective
Apply multiple Python concepts learned in previous tasks to create a functional task management application.

## Instructions
Create a command-line task manager application with the following features:
1. Add tasks with title, description, due date, and priority
2. View all tasks
3. Mark tasks as complete
4. Delete tasks
5. Filter tasks by status (complete/incomplete) or priority
6. Save tasks to a file and load them when the program starts
7. Implement error handling for user input
8. Organize code using functions and classes
9. Create a simple menu-driven interface

## Concepts to Apply
- Variables and data types
- Control flow (if statements, loops)
- Functions
- Lists and dictionaries
- File I/O (JSON or CSV)
- Error handling
- Object-oriented programming
- Modules and imports
- Date handling
- User input validation

## Expected Output
```
TASK MANAGER
============
1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Delete Task
5. Filter Tasks
6. Exit

Enter your choice: 1

Add a new task:
Title: Complete Python Project
Description: Finish the mini project for the Python course
Due date (YYYY-MM-DD): 2025-09-01
Priority (High/Medium/Low): High

Task added successfully!

TASK MANAGER
============
1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Delete Task
5. Filter Tasks
6. Exit

Enter your choice: 2

TASKS:
------
1. [Incomplete] Complete Python Project (High)
   Due: 2025-09-01
   Description: Finish the mini project for the Python course

TASK MANAGER
============
...
```

## Tips
- Plan your data structure before starting to code
- Use a dictionary to represent each task
- Use a list to store all tasks
- Use the `datetime` module for handling dates
- Save tasks in JSON format for easy storage and retrieval
- Create a `Task` class to represent tasks
- Implement input validation to handle incorrect user input
- Use functions to organize your code
- Consider creating a separate module for task-related operations
- Test your application thoroughly with different inputs and edge cases
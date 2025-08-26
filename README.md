# Learn Python

A comprehensive, structured learning path for Python programming, from basics to advanced concepts.

## Overview

This repository contains a series of progressive tasks designed to help you learn Python programming from scratch. Each task builds upon the previous ones, gradually introducing more complex concepts and real-world applications.

The learning path consists of 11 tasks:

1. **Hello World**: Basic syntax, printing, and variables
2. **Data Types**: Working with different data types and type conversions
3. **Control Flow**: Conditionals, loops, and logical operations
4. **Functions**: Creating and using functions, parameters, and return values
5. **Collections**: Working with lists and dictionaries
6. **File I/O**: Reading from and writing to files
7. **Error Handling**: Try-except blocks and custom exceptions
8. **Object-Oriented Programming**: Classes, inheritance, and polymorphism
9. **Modules and Packages**: Organizing code and importing functionality
10. **Mini Project**: Command-line Task Manager
11. **FastAPI Task Manager**: Web API development with FastAPI

Each task includes a detailed description and a starter Python file with comments and placeholders to guide you through the implementation.

## Getting Started

### Forking the Repository

To create your own copy of this repository:

1. Click the "Fork" button at the top right of this repository page on GitHub
2. This will create a copy of the repository in your GitHub account
3. Clone your forked repository to your local machine:

```bash
git clone https://github.com/YOUR_USERNAME/learn-python.git
cd learn-python
```

### Setting Up a Virtual Environment

A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus additional packages. Using a virtual environment for this project is recommended because:

- It keeps dependencies required by different projects separate
- It avoids conflicts between package versions
- It ensures you have the correct versions of packages needed for these tasks
- It makes it easier to share your code with others

#### Creating a Virtual Environment

1. Make sure you have Python 3.6+ installed on your system
2. Open a terminal/command prompt and navigate to the repository directory
3. Create a virtual environment:

```bash
# On macOS/Linux
python3 -m venv env

# On Windows
python -m venv env
```

4. Activate the virtual environment:

```bash
# On macOS/Linux
source env/bin/activate

# On Windows
env\Scripts\activate
```

5. Your command prompt should now show the name of the virtual environment, indicating it's active

#### Installing Dependencies

Some tasks (especially Task 11) require additional packages. Install them with:

```bash
pip install -r requirements.txt
```

If there's no requirements.txt file, you can install packages as needed:

```bash
# For Task 11
pip install fastapi uvicorn
```

### Running Task Files

Each task has its own directory with a Python file that you need to complete and run. To run a task file:

1. Make sure your virtual environment is activated
2. Navigate to the task directory
3. Run the Python file:

```bash
# Example for Task 1
cd tasks/task1_hello_world
python hello_world.py
```

For Task 11 (FastAPI Task Manager), you'll need to run it with Uvicorn:

```bash
cd tasks/task11_fastapi_task_manager
uvicorn task_manager_api:app --reload
```

Then open your browser to http://127.0.0.1:8000/docs to see the API documentation.

## Repository Structure

```
learn-python/
├── README.md
├── requirements.txt (if needed)
├── tasks/
│   ├── task1_hello_world/
│   │   ├── description.md
│   │   └── hello_world.py
│   ├── task2_data_types/
│   │   ├── description.md
│   │   └── data_types.py
│   ├── ...
│   ├── task10_mini_project/
│   │   ├── description.md
│   │   └── task_manager.py
│   └── task11_fastapi_task_manager/
│       ├── description.md
│       └── task_manager_api.py
```

## Task Descriptions

### Task 1: Hello World
Introduction to basic Python syntax, printing to the console, and working with variables. Includes a real-world task to create a personal information card.

### Task 2: Data Types
Learn about different data types in Python and how to work with them. Includes a temperature converter application.

### Task 3: Control Flow
Learn how to control the flow of your program using conditional statements and loops. Includes a text-based adventure game.

### Task 4: Functions
Learn how to create and use functions to organize code and improve reusability. Includes a date and time utility library.

### Task 5: Collections
Learn how to work with Python's collection data types, focusing on lists and dictionaries. Includes a contact management system.

### Task 6: File I/O
Learn how to read from and write to files in Python. Includes a note-taking application.

### Task 7: Error Handling
Learn how to handle errors and exceptions in Python. Includes a form data validator.

### Task 8: Object-Oriented Programming
Learn the principles of object-oriented programming in Python. Includes a library management system.

### Task 9: Modules and Packages
Learn how to organize code using modules and packages. Includes a scientific calculator package.

### Task 10: Mini Project - Task Manager
Apply multiple Python concepts to create a functional task management application.

### Task 11: FastAPI Task Manager
Transform the Task Manager from Task 10 into a web API using FastAPI.

## Contributing

If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
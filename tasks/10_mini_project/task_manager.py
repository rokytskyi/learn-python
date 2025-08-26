# Task 10: Mini Project - Task Manager
# This is a starter file for the Task Manager application
# Complete the code to implement all the required features

import json
import datetime
from typing import List, Dict, Any, Optional

# Task class to represent a task
class Task:
    """Class representing a task in the task manager."""
    
    def __init__(self, title: str, description: str, due_date: str, priority: str):
        """Initialize a new task with the given attributes."""
        # Your code here:
        pass
    
    def mark_complete(self):
        """Mark the task as complete."""
        # Your code here:
        pass
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the task to a dictionary for JSON serialization."""
        # Your code here:
        pass
    
    @classmethod
    def from_dict(cls, task_dict: Dict[str, Any]) -> 'Task':
        """Create a Task object from a dictionary."""
        # Your code here:
        pass
    
    def __str__(self) -> str:
        """Return a string representation of the task."""
        # Your code here:
        pass


# TaskManager class to manage tasks
class TaskManager:
    """Class for managing tasks."""
    
    def __init__(self, filename: str = "tasks.json"):
        """Initialize the task manager with the given filename."""
        # Your code here:
        pass
    
    def add_task(self, title: str, description: str, due_date: str, priority: str) -> bool:
        """Add a new task to the task list."""
        # Your code here:
        pass
    
    def view_tasks(self) -> List[Task]:
        """Return all tasks."""
        # Your code here:
        pass
    
    def mark_task_complete(self, task_index: int) -> bool:
        """Mark the task at the given index as complete."""
        # Your code here:
        pass
    
    def delete_task(self, task_index: int) -> bool:
        """Delete the task at the given index."""
        # Your code here:
        pass
    
    def filter_tasks(self, status: Optional[bool] = None, priority: Optional[str] = None) -> List[Task]:
        """Filter tasks by status and/or priority."""
        # Your code here:
        pass
    
    def save_tasks(self) -> bool:
        """Save tasks to the JSON file."""
        # Your code here:
        pass
    
    def load_tasks(self) -> bool:
        """Load tasks from the JSON file."""
        # Your code here:
        pass


# UI functions
def display_menu():
    """Display the main menu."""
    print("\nTASK MANAGER")
    print("============")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Filter Tasks")
    print("6. Exit")


def get_user_choice() -> int:
    """Get the user's menu choice."""
    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def add_task_ui(task_manager: TaskManager):
    """UI for adding a task."""
    # Your code here:
    while True:
        try:
            choice = str(input("\nEnter task title: "))

            # save entered task task

            print(f'Task with title "{choice}" was added.')
            return
        except ValueError:
            print("Invalid input. Please enter a string.")


def view_tasks_ui(task_manager: TaskManager):
    """UI for viewing tasks."""
    # Your code here:
    pass


def mark_task_complete_ui(task_manager: TaskManager):
    """UI for marking a task as complete."""
    # Your code here:
    pass


def delete_task_ui(task_manager: TaskManager):
    """UI for deleting a task."""
    # Your code here:
    pass


def filter_tasks_ui(task_manager: TaskManager):
    """UI for filtering tasks."""
    # Your code here:
    pass


def main():
    """Main function to run the task manager."""
    task_manager = TaskManager()
    task_manager.load_tasks()
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 1:
            add_task_ui(task_manager)
        elif choice == 2:
            view_tasks_ui(task_manager)
        elif choice == 3:
            mark_task_complete_ui(task_manager)
        elif choice == 4:
            delete_task_ui(task_manager)
        elif choice == 5:
            filter_tasks_ui(task_manager)
        elif choice == 6:
            print("Exiting Task Manager. Goodbye!")
            break
        
        task_manager.save_tasks()


if __name__ == "__main__":
    main()
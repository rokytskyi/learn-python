# my_module.py
# This is a sample module for Task 9

def greet(name):
    """Return a greeting message with the given name."""
    return f"Hello, {name}!"

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

class Person:
    """A simple class representing a person."""
    
    def __init__(self, name, age):
        """Initialize a Person with a name and age."""
        self.name = name
        self.age = age
    
    def introduce(self):
        """Return an introduction string."""
        return f"My name is {self.name} and I am {self.age} years old."

# This code runs only when the module is executed directly
if __name__ == "__main__":
    print("This module is being run directly.")
    print(greet("World"))
else:
    print("This module has been imported.")
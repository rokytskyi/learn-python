# Task 9: Modules and Packages
# Complete the exercises below

# 1. Import and use built-in Python modules
# Your code here:
# Example:
# import math
# import random
# import datetime
# import os
# import sys
# 
# # Using the math module
# print("Math module examples:")
# print(f"Pi: {math.pi}")
# print(f"Square root of 16: {math.sqrt(16)}")
# print(f"Cosine of 0: {math.cos(0)}")
# 
# # Using the random module
# print("\nRandom module examples:")
# print(f"Random number between 0 and 1: {random.random()}")
# print(f"Random integer between 1 and 10: {random.randint(1, 10)}")
# print(f"Random choice from a list: {random.choice(['apple', 'banana', 'cherry'])}")
# 
# # Using the datetime module
# print("\nDatetime module examples:")
# now = datetime.datetime.now()
# print(f"Current date and time: {now}")
# print(f"Formatted date: {now.strftime('%Y-%m-%d')}")
# 
# # Using the os module
# print("\nOS module examples:")
# print(f"Current working directory: {os.getcwd()}")
# print(f"List of files in current directory: {os.listdir('.')}")
# 
# # Using the sys module
# print("\nSys module examples:")
# print(f"Python version: {sys.version}")
# print(f"Module search paths: {sys.path}")


# 2. Create your own module with functions and classes
# Your code here:
# Example:
# # First, create a file named 'my_module.py' with the following content:
# """
# # my_module.py
# 
# def greet(name):
#     return f"Hello, {name}!"
# 
# def add(a, b):
#     return a + b
# 
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     
#     def introduce(self):
#         return f"My name is {self.name} and I am {self.age} years old."
# 
# # This code runs only when the module is executed directly
# if __name__ == "__main__":
#     print("This module is being run directly.")
#     print(greet("World"))
# else:
#     print("This module has been imported.")
# """
# 
# # Then, in this file, import and use the module:
# import my_module
# 
# print("\nCustom module examples:")
# print(f"Greeting: {my_module.greet('Alice')}")
# print(f"Addition: {my_module.add(5, 3)}")
# 
# person = my_module.Person("Bob", 30)
# print(f"Person introduction: {person.introduce()}")


# 3. Import specific functions or classes from modules
# Your code here:
# Example:
# # Selective imports
# from math import pi, sqrt
# from random import randint, choice
# from datetime import datetime
# 
# print("\nSelective import examples:")
# print(f"Pi: {pi}")
# print(f"Square root of 25: {sqrt(25)}")
# print(f"Random integer between 1 and 6: {randint(1, 6)}")
# print(f"Random choice: {choice(['red', 'green', 'blue'])}")
# print(f"Current time: {datetime.now().strftime('%H:%M:%S')}")
# 
# # From your custom module
# from my_module import greet, Person
# 
# print(greet("Charlie"))
# person2 = Person("Dave", 25)
# print(person2.introduce())


# 4. Use module aliases
# Your code here:
# Example:
# # Module aliases
# import math as m
# import random as r
# import datetime as dt
# import my_module as mm
# 
# print("\nModule alias examples:")
# print(f"Pi using alias: {m.pi}")
# print(f"Random number using alias: {r.random()}")
# print(f"Current year using alias: {dt.datetime.now().year}")
# print(f"Greeting using alias: {mm.greet('Eve')}")


# 5. Create a package with multiple modules
# Your code here:
# Example:
# # First, create a package directory structure:
# # my_package/
# # ├── __init__.py
# # ├── module1.py
# # └── module2.py
# 
# """
# # my_package/__init__.py
# print("Initializing my_package")
# 
# # You can define what gets imported when someone does "from my_package import *"
# __all__ = ['module1', 'module2']
# """
# 
# """
# # my_package/module1.py
# def function1():
#     return "This is function1 from module1"
# 
# class Class1:
#     def method1(self):
#         return "This is method1 from Class1 in module1"
# """
# 
# """
# # my_package/module2.py
# def function2():
#     return "This is function2 from module2"
# 
# class Class2:
#     def method2(self):
#         return "This is method2 from Class2 in module2"
# """
# 
# # Then, import and use the package:
# import my_package
# from my_package import module1, module2
# 
# print("\nPackage examples:")
# print(module1.function1())
# obj1 = module1.Class1()
# print(obj1.method1())
# 
# print(module2.function2())
# obj2 = module2.Class2()
# print(obj2.method2())


# 6. Understand module search paths
# Your code here:
# Example:
# import sys
# 
# print("\nModule search paths:")
# for path in sys.path:
#     print(f"- {path}")
# 
# # You can add a new directory to the search path
# # sys.path.append('/path/to/your/modules')
# # print("\nUpdated module search paths:")
# # for path in sys.path:
# #     print(f"- {path}")


# 7. Explore the `__name__ == "__main__"` pattern
# Your code here:
# Example:
# # Create a file named 'main_demo.py' with the following content:
# """
# # main_demo.py
# 
# def main_function():
#     print("This is the main function.")
#     print("It contains the main logic of the program.")
#     return "Main function executed successfully"
# 
# # This code only runs when the script is executed directly
# if __name__ == "__main__":
#     print("This script is being run directly.")
#     result = main_function()
#     print(f"Result: {result}")
# else:
#     print("This script has been imported as a module.")
# """
# 
# # Run the file directly to see one behavior
# # Then import it to see different behavior:
# import main_demo
# 
# print("\nTrying to call the main function from the imported module:")
# result = main_demo.main_function()
# print(f"Result when called from import: {result}")
# my_package/__init__.py
# This file marks the directory as a Python package

print("Initializing my_package")

# You can define what gets imported when someone does "from my_package import *"
__all__ = ['module1', 'module2']
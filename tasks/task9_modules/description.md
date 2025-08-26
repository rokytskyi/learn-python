# Task 9: Modules and Packages

## Objective
Learn how to organize code using modules and packages, import functionality from other modules, and create your own reusable modules.

## Instructions
1. Import and use built-in Python modules
2. Create your own module with functions and classes
3. Import specific functions or classes from modules
4. Use module aliases
5. Create a package with multiple modules
6. Understand module search paths
7. Explore the `__name__ == "__main__"` pattern

## Concepts to Learn
- Module imports (`import` statement)
- Selective imports (`from module import name`)
- Module aliases (`import module as alias`)
- Creating modules
- Creating packages with `__init__.py`
- Module search path (`sys.path`)
- The `if __name__ == "__main__"` idiom
- Relative vs. absolute imports
- Reloading modules
- Common built-in modules (os, sys, math, datetime, random, etc.)

## Expected Output
```
Built-in modules:
[Output showing usage of built-in modules]

Custom module:
[Output showing creation and usage of a custom module]

Selective imports:
[Output demonstrating selective imports]

Module aliases:
[Output showing module aliasing]

Package creation:
[Output demonstrating package usage]

Module search paths:
[Output showing module search paths]

Main module pattern:
[Output showing the __name__ == "__main__" pattern]
```

## Real-World Task: Scientific Calculator Package

Create a modular scientific calculator package with different calculation modules organized into a coherent package structure. This task will help you apply module and package concepts in a practical context that can be verified.

### Requirements:
1. Create a calculator package with the following modules:
   - `basic.py`: Basic arithmetic operations (addition, subtraction, multiplication, division)
   - `scientific.py`: Scientific operations (power, square root, logarithm, trigonometric functions)
   - `statistics.py`: Statistical operations (mean, median, mode, standard deviation)
   - `conversions.py`: Unit conversions (temperature, length, weight, etc.)
   - `financial.py`: Financial calculations (compound interest, loan payments, etc.)

2. Implement the package structure:
   - Create a proper package structure with `__init__.py` files
   - Use relative imports within the package
   - Expose key functions at the package level for easy access
   - Include version information in the package

3. For each module:
   - Implement appropriate functions with proper documentation
   - Include error handling for invalid inputs
   - Add examples in docstrings
   - Create a `__name__ == "__main__"` section for testing

4. Create a main script that:
   - Imports and uses functions from different modules
   - Provides a simple command-line interface
   - Demonstrates different import techniques
   - Shows how to use the package as a whole

### Verification Criteria:
Your calculator package should:
- Have a proper package structure with `__init__.py` files
- Include at least 5 different modules with related functionality
- Implement at least 3-5 functions in each module
- Use proper docstrings and comments
- Handle errors gracefully
- Be importable as a whole package or as individual modules
- Demonstrate different import techniques
- Include a main script that shows how to use the package
- Have a `__name__ == "__main__"` section in each module for testing
- Be well-organized and maintainable

### Example Usage:
```python
# Importing the entire package
import calculator
result = calculator.add(5, 3)  # Using a function exposed at package level
print(f"5 + 3 = {result}")

# Importing specific modules
from calculator import scientific
sin_value = scientific.sin(0.5)
print(f"sin(0.5) = {sin_value}")

# Using module aliases
import calculator.statistics as stats
data = [1, 2, 3, 4, 5]
mean_value = stats.mean(data)
print(f"Mean of {data} = {mean_value}")

# Using the main script
# $ python calculator_app.py
# Scientific Calculator
# ====================
# 1. Basic Operations
# 2. Scientific Operations
# 3. Statistical Operations
# 4. Unit Conversions
# 5. Financial Calculations
# 6. Exit
# 
# Enter your choice: 1
# 
# Basic Operations
# ---------------
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 
# Enter your choice: 1
# Enter first number: 10
# Enter second number: 5
# Result: 10 + 5 = 15
```

## Tips
- Modules are just Python files (`.py`)
- Packages are directories containing modules and an `__init__.py` file
- The `__init__.py` file can be empty but is required for a directory to be recognized as a package in Python < 3.3
- Use `dir(module)` to see what's available in a module
- Use `help(module)` to get documentation for a module
- The `if __name__ == "__main__"` pattern allows a file to be both imported as a module and run as a script
- Avoid circular imports (module A imports module B, which imports module A)
- Use relative imports (`.module`) within packages
- The module search path includes the current directory, installed packages, and directories in `PYTHONPATH`
- Common built-in modules include `os`, `sys`, `math`, `datetime`, `random`, `json`, and `re`
- Consider using type hints to make your code more readable
- Use docstrings to document your modules, classes, and functions
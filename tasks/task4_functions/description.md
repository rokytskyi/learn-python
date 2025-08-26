# Task 4: Functions

## Objective
Learn how to create and use functions to organize code, improve reusability, and make your programs more modular.

## Instructions
1. Create a simple function that takes no parameters and returns a greeting
2. Write a function that takes parameters and returns a calculated value
3. Create a function with default parameter values
4. Implement a function that uses keyword arguments
5. Create a function that returns multiple values
6. Write a recursive function (e.g., factorial or Fibonacci)

## Concepts to Learn
- Function definition with `def`
- Parameters and arguments
- Return values
- Default parameter values
- Keyword arguments
- Positional vs. keyword arguments
- Returning multiple values
- Scope of variables (local vs. global)
- Recursion

## Expected Output
```
Simple function:
[Output from a function with no parameters]

Function with parameters:
[Output from a function with parameters]

Function with default parameters:
[Output showing default and custom values]

Function with keyword arguments:
[Output showing keyword argument usage]

Function returning multiple values:
[Output showing multiple returned values]

Recursive function:
[Output from a recursive function]
```

## Real-World Task: Date and Time Utility Library

Create a utility library with functions for working with dates, times, and time intervals. This task will help you apply function concepts in a practical context that can be verified.

### Requirements:
1. Create a collection of functions that handle various date and time operations:
   - A function that returns the current date and time in a formatted string
   - A function that converts between different time units (seconds, minutes, hours, days)
   - A function with default parameters that formats a date in different styles
   - A function that calculates the time difference between two dates
   - A function that returns multiple values about a given date (day of week, day of year, week number)
   - A recursive function that calculates a future date after adding a specified number of business days (skipping weekends)

2. Each function should:
   - Have a clear purpose and descriptive name
   - Include proper docstrings explaining what the function does, its parameters, and return values
   - Handle parameters appropriately (using default values, keyword arguments where appropriate)
   - Return meaningful values

### Verification Criteria:
Your utility library should:
- Include at least 6 different functions covering the requirements
- Have proper documentation for each function
- Handle parameters correctly (positional, keyword, default values)
- Return correct results for various inputs
- Include at least one function that returns multiple values
- Include at least one recursive function
- Be usable as a practical tool for date and time operations

### Example Usage:
```python
# Get current date and time in a formatted string
current_time = get_formatted_time()
print(f"Current time: {current_time}")  # Output: Current time: August 26, 2025 - 14:30:45

# Convert between time units
minutes = convert_time(2, from_unit="hours", to_unit="minutes")
print(f"2 hours = {minutes} minutes")  # Output: 2 hours = 120 minutes

# Format a date in different styles
date_str = format_date(2025, 8, 26, style="short")
print(f"Formatted date: {date_str}")  # Output: Formatted date: 08/26/25

# Calculate time difference
days_until = calculate_time_difference("2025-12-25", "2025-08-26", unit="days")
print(f"Days until Christmas: {days_until}")  # Output: Days until Christmas: 121

# Get multiple date components
weekday, day_of_year, week_num = get_date_components("2025-08-26")
print(f"August 26, 2025 is a {weekday}, day {day_of_year} of the year, in week {week_num}")

# Calculate a future business date (recursive function)
future_date = add_business_days("2025-08-26", 10)
print(f"10 business days after August 26, 2025: {future_date}")
```

## Tips
- Functions should do one thing and do it well
- Use descriptive function names (verb_noun format is common)
- Document your functions with docstrings
- Be careful with mutable default arguments
- Return values are optional, but most functions should return something
- Functions can return multiple values as a tuple
- Recursive functions need a base case to avoid infinite recursion
- Variables defined inside a function are local to that function
- Use `global` keyword to modify global variables from within a function (but use sparingly)
- The `datetime` module in Python is useful for working with dates and times
- Consider using type hints to indicate parameter and return types
# Task 4: Functions
# Complete the exercises below

# 1. Create a simple function that takes no parameters and returns a greeting
# Your code here:
# Example:
# def say_hello():
#     """Return a simple greeting message."""
#     return "Hello, world!"
# 
# # Call the function
# greeting = say_hello()
# print(greeting)


# 2. Write a function that takes parameters and returns a calculated value
# Your code here:
# Example:
# def calculate_area(length, width):
#     """Calculate the area of a rectangle."""
#     return length * width
# 
# # Call the function
# area = calculate_area(5, 3)
# print(f"The area is {area} square units")


# 3. Create a function with default parameter values
# Your code here:
# Example:
# def make_coffee(type="latte", size="medium", sugar=True):
#     """Prepare a coffee with specified parameters."""
#     result = f"Making a {size} {type}"
#     if sugar:
#         result += " with sugar"
#     return result
# 
# # Call the function with different combinations
# print(make_coffee())  # Uses all defaults
# print(make_coffee("espresso", "small", False))  # No defaults


# 4. Implement a function that uses keyword arguments
# Your code here:
# Example:
# def create_profile(name, age, city="Unknown", hobby="Unknown"):
#     """Create a user profile."""
#     return {
#         "name": name,
#         "age": age,
#         "city": city,
#         "hobby": hobby
#     }
# 
# # Call the function with keyword arguments
# profile = create_profile(name="Alice", age=30, hobby="Painting")
# print(profile)


# 5. Create a function that returns multiple values
# Your code here:
# Example:
# def get_dimensions():
#     """Return width, height, and depth of an object."""
#     width = 10
#     height = 20
#     depth = 15
#     return width, height, depth
# 
# # Call the function and unpack the returned values
# w, h, d = get_dimensions()
# print(f"Width: {w}, Height: {h}, Depth: {d}")


# 6. Write a recursive function (e.g., factorial or Fibonacci)
# Your code here:
# Example:
# def factorial(n):
#     """Calculate the factorial of n using recursion."""
#     # Base case
#     if n == 0 or n == 1:
#         return 1
#     # Recursive case
#     else:
#         return n * factorial(n - 1)
# 
# # Call the recursive function
# result = factorial(5)  # 5! = 5 * 4 * 3 * 2 * 1 = 120
# print(f"Factorial of 5 is {result}")


# Real-World Task: Date and Time Utility Library
# This task will help you apply function concepts in a practical context.

# Import the datetime module to work with dates and times
# import datetime

# 1. Function that returns the current date and time in a formatted string
def get_formatted_time(format_string="%B %d, %Y - %H:%M:%S"):
    """
    Return the current date and time as a formatted string.
    
    Args:
        format_string (str): The format to use for the date and time.
                            Default is "%B %d, %Y - %H:%M:%S" (e.g., "August 26, 2025 - 14:30:45")
    
    Returns:
        str: The formatted current date and time.
    """
    # Your code here:
    pass

# 2. Function that converts between different time units
def convert_time(value, from_unit="hours", to_unit="minutes"):
    """
    Convert a time value from one unit to another.
    
    Args:
        value (float): The time value to convert.
        from_unit (str): The unit to convert from. Options: "seconds", "minutes", "hours", "days".
        to_unit (str): The unit to convert to. Options: "seconds", "minutes", "hours", "days".
    
    Returns:
        float: The converted time value.
    
    Raises:
        ValueError: If an invalid unit is provided.
    """
    # Your code here:
    pass

# 3. Function with default parameters that formats a date in different styles
def format_date(year, month, day, style="medium"):
    """
    Format a date in different styles.
    
    Args:
        year (int): The year.
        month (int): The month (1-12).
        day (int): The day of the month.
        style (str): The formatting style. Options: "short", "medium", "long", "iso".
                    Default is "medium".
    
    Returns:
        str: The formatted date string.
    
    Examples:
        - Short style: "08/26/25"
        - Medium style: "Aug 26, 2025"
        - Long style: "August 26, 2025"
        - ISO style: "2025-08-26"
    """
    # Your code here:
    pass

# 4. Function that calculates the time difference between two dates
def calculate_time_difference(date1, date2, unit="days"):
    """
    Calculate the time difference between two dates.
    
    Args:
        date1 (str): The first date in format "YYYY-MM-DD".
        date2 (str): The second date in format "YYYY-MM-DD".
        unit (str): The unit for the result. Options: "days", "hours", "minutes", "seconds".
                   Default is "days".
    
    Returns:
        float: The time difference in the specified unit.
    """
    # Your code here:
    pass

# 5. Function that returns multiple values about a given date
def get_date_components(date_str):
    """
    Get various components of a given date.
    
    Args:
        date_str (str): The date in format "YYYY-MM-DD".
    
    Returns:
        tuple: A tuple containing:
            - weekday (str): The day of the week (e.g., "Monday").
            - day_of_year (int): The day of the year (1-366).
            - week_number (int): The week number of the year (1-53).
    """
    # Your code here:
    pass

# 6. Recursive function that calculates a future date after adding business days
def add_business_days(date_str, days):
    """
    Calculate a future date after adding a specified number of business days (skipping weekends).
    
    Args:
        date_str (str): The starting date in format "YYYY-MM-DD".
        days (int): The number of business days to add.
    
    Returns:
        str: The resulting date in format "YYYY-MM-DD".
    """
    # Your code here:
    # Hint: Use recursion to handle the case of adding one business day at a time
    pass

# Test your functions
def test_date_time_library():
    """Test the date and time utility functions."""
    print("Date and Time Utility Library Tests\n")
    
    # Test get_formatted_time
    print("1. Current formatted time:")
    current_time = get_formatted_time()
    print(f"   {current_time}")
    
    # Test convert_time
    print("\n2. Time conversion:")
    minutes = convert_time(2, from_unit="hours", to_unit="minutes")
    print(f"   2 hours = {minutes} minutes")
    
    # Test format_date
    print("\n3. Date formatting:")
    short_date = format_date(2025, 8, 26, style="short")
    medium_date = format_date(2025, 8, 26)  # Default style
    long_date = format_date(2025, 8, 26, style="long")
    print(f"   Short: {short_date}")
    print(f"   Medium: {medium_date}")
    print(f"   Long: {long_date}")
    
    # Test calculate_time_difference
    print("\n4. Time difference:")
    days_diff = calculate_time_difference("2025-12-25", "2025-08-26", unit="days")
    print(f"   Days between Aug 26 and Dec 25, 2025: {days_diff}")
    
    # Test get_date_components
    print("\n5. Date components:")
    weekday, day_of_year, week_num = get_date_components("2025-08-26")
    print(f"   August 26, 2025 is a {weekday}, day {day_of_year} of the year, in week {week_num}")
    
    # Test add_business_days
    print("\n6. Adding business days:")
    future_date = add_business_days("2025-08-26", 10)
    print(f"   10 business days after August 26, 2025: {future_date}")

# Uncomment to run the tests
# test_date_time_library()
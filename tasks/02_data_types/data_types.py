# Task 2: Data Types
# Complete the exercises below

# 1. Create variables with the following data types
# Your code here:
# Integer
# my_integer = 42

# Float
# my_float = 3.14

# String
# my_string = "Hello Python"

# Boolean
# my_boolean = True

# Print all variables with their types
# print("Integer:", my_integer)
# print("Float:", my_float)
# print("String:", my_string)
# print("Boolean:", my_boolean)

# print("\nType conversion examples:")
# 2. Demonstrate type conversion between different data types
# Your code here:
# Example: Convert string to integer
# num_string = "42"
# num_integer = int(num_string)
# print(f"'{num_string}' converted to integer: {num_integer}")


# print("\nString operations:")
# 3. Perform string operations (concatenation, slicing, methods)
# Your code here:
# Example: String concatenation
# first_name = "Python"
# last_name = "Learner"
# full_name = first_name + " " + last_name
# print(f"Concatenated string: {full_name}")


# print("\nArithmetic operations:")
# 4. Use arithmetic operators with numbers
# Your code here:
# Example: Addition, subtraction, multiplication, division
# a = 10
# b = 3
# print(f"{a} + {b} = {a + b}")


# print("\nComparison results:")
# 5. Demonstrate the use of comparison operators
# Your code here:
# Example: Equal to, greater than
# x = 5
# y = 10
# print(f"{x} == {y}: {x == y}")
# print(f"{x} < {y}: {x < y}")


# Real-World Task: Temperature Converter
# This task will help you apply data types, type conversion, arithmetic operations, 
# and comparison operators in a practical context.

# 1. Display a menu for temperature conversion options
def display_menu():
    print("\nTEMPERATURE CONVERTER")
    print("\nSelect conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

# 2. Get user choice and temperature value
# Your code here:
# Example:
# choice = input("\nEnter your choice (1-6): ")
# temperature = input("Enter temperature: ")

# 3. Convert the temperature based on the selected option
# Your code here:

# 4. Determine the temperature description (freezing, room temperature, boiling)
# Your code here:

# 5. Display the result with appropriate formatting
# Your code here:

# 6. Main program
# Your code here:
# Example:

# display_menu()
# try:
#     choice = int(input("\nEnter your choice (1-6): "))
#     if 1 <= choice <= 6:
#     # Get temperature and convert based on choice
#     # Display result with formatting
#     else:
#         print("Invalid choice. Please enter a number between 1 and 6.")
# except ValueError:
#     print("Invalid input. Please enter a number.")
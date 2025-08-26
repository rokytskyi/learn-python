# Task 1: Hello World

## Objective
Learn the basics of Python syntax, printing to the console, and working with variables.

## Instructions
1. Print "Hello, World!" to the console
2. Create a variable with your name and print a greeting using that variable
3. Create two number variables and print their sum
4. Print the current date (you can use a string for this)

## Concepts to Learn
- Basic Python syntax
- The `print()` function
- Variables and assignment
- String formatting with f-strings
- Basic arithmetic operations

## Expected Output
```
Hello, World!
Hello, [your name]!
[sum of your numbers]
Today is [date]
```

## Real-World Task: Personal Information Card
Create a program that displays a formatted personal information card. This task will help you apply basic printing, variable usage, and string formatting in a practical context.

### Requirements:
1. Ask the user for their name, age, city, and a fun fact about themselves
2. Calculate the birth year based on the current year (2025) and the age provided
3. Format and display all this information as a nicely formatted "Personal Info Card"
4. Include the current date at the bottom of the card

### Verification Criteria:
Your program should:
- Accept user input for all required fields
- Correctly calculate the birth year
- Display a formatted card with all information
- Include proper spacing and formatting to make the card readable
- Show the current date at the bottom

### Example Output:
```
===================================
        PERSONAL INFO CARD
===================================
Name: John Smith
Age: 25
City: New York
Birth Year: 2000
Fun Fact: I can solve a Rubik's cube in under 2 minutes

Created on: August 26, 2025
===================================
```

## Tips
- Use the `print()` function to display output
- Variables don't need type declarations in Python
- You can use the `+` operator to add numbers
- F-strings (formatted string literals) use the syntax: f"Text {variable}"
- Use the `input()` function to get user input
- To calculate the birth year: current_year - age
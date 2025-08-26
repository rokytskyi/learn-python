# Task 2: Data Types

## Objective
Learn about different data types in Python and how to work with them.

## Instructions
1. Create variables with the following data types:
   - Integer
   - Float
   - String
   - Boolean
2. Demonstrate type conversion between different data types
3. Perform string operations (concatenation, slicing, methods)
4. Use arithmetic operators with numbers
5. Demonstrate the use of comparison operators

## Concepts to Learn
- Basic data types in Python
- Type conversion functions (`int()`, `float()`, `str()`, `bool()`)
- String operations and methods
- Arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
- Comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)

## Expected Output
```
Integer: [your integer]
Float: [your float]
String: [your string]
Boolean: [your boolean]

Type conversion examples:
[Show examples of converting between types]

String operations:
[Show examples of string operations]

Arithmetic operations:
[Show examples of arithmetic operations]

Comparison results:
[Show examples of comparison operations]
```

## Real-World Task: Temperature Converter

Create a temperature conversion program that converts between Celsius, Fahrenheit, and Kelvin. This task will help you apply data types, type conversion, arithmetic operations, and comparison operators in a practical context.

### Requirements:
1. Create a menu that allows the user to select a conversion type:
   - Celsius to Fahrenheit
   - Fahrenheit to Celsius
   - Celsius to Kelvin
   - Kelvin to Celsius
   - Fahrenheit to Kelvin
   - Kelvin to Fahrenheit
2. Get the temperature value from the user
3. Perform the conversion using the appropriate formula
4. Display the result with appropriate formatting
5. Include a comparison that tells the user if the converted temperature is:
   - Below freezing (0°C / 32°F / 273.15K)
   - Room temperature (around 20-25°C / 68-77°F / 293-298K)
   - Boiling point of water (100°C / 212°F / 373.15K)

### Conversion Formulas:
- Celsius to Fahrenheit: (C × 9/5) + 32
- Fahrenheit to Celsius: (F - 32) × 5/9
- Celsius to Kelvin: C + 273.15
- Kelvin to Celsius: K - 273.15
- Fahrenheit to Kelvin: (F - 32) × 5/9 + 273.15
- Kelvin to Fahrenheit: (K - 273.15) × 9/5 + 32

### Verification Criteria:
Your program should:
- Accept user input for conversion type and temperature value
- Correctly apply the conversion formula
- Display the result with appropriate units
- Provide accurate comparison information about the temperature
- Handle different data types appropriately (convert string input to numeric)
- Format the output to 2 decimal places

### Example Output:
```
TEMPERATURE CONVERTER

Select conversion type:
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Fahrenheit to Kelvin
6. Kelvin to Fahrenheit

Enter your choice (1-6): 1
Enter temperature in Celsius: 25

RESULT:
25.00°C = 77.00°F
This temperature is at room temperature.
```

## Tips
- Use the `type()` function to check the data type of a variable
- Strings can be sliced using the syntax `string[start:end]`
- Common string methods include `.upper()`, `.lower()`, `.strip()`, `.replace()`
- Integer division uses the `//` operator
- The modulo operator `%` gives the remainder of division
- The exponentiation operator is `**`
- Use the `float()` function to convert input to a floating-point number
- Format floating-point numbers using f-strings: f"{value:.2f}"
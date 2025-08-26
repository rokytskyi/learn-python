# Task 7: Error Handling
# Complete the exercises below

# 1. Understand different types of errors
# Examples of common errors (commented out to prevent actual errors):

# Syntax Error:
# def function_with_syntax_error()
#     print("Missing colon after function definition")

# Runtime Error (ZeroDivisionError):
# result = 10 / 0

# Type Error:
# text = "hello"
# number = 5
# combined = text + number  # Can't concatenate str and int

# Index Error:
# my_list = [1, 2, 3]
# item = my_list[10]  # Index out of range

# Key Error:
# my_dict = {"name": "Alice", "age": 30}
# value = my_dict["address"]  # Key doesn't exist


# 2. Use try-except blocks to catch and handle exceptions
# Your code here:
# Example:
# try:
#     # Code that might raise an exception
#     number = int(input("Enter a number: "))
#     result = 100 / number
#     print(f"100 divided by {number} is {result}")
# except:
#     # Handle the exception
#     print("An error occurred")


# 3. Handle multiple exception types
# Your code here:
# Example:
# try:
#     # Code that might raise different exceptions
#     number = int(input("Enter a number: "))
#     result = 100 / number
#     print(f"100 divided by {number} is {result}")
#     
#     my_list = [1, 2, 3]
#     index = int(input("Enter an index: "))
#     value = my_list[index]
#     print(f"Value at index {index} is {value}")
# except ValueError:
#     # Handle ValueError (e.g., invalid input for int conversion)
#     print("Invalid input: Please enter a valid number")
# except ZeroDivisionError:
#     # Handle division by zero
#     print("Error: Cannot divide by zero")
# except IndexError:
#     # Handle index out of range
#     print(f"Error: Index out of range. List has {len(my_list)} items")
# except Exception as e:
#     # Handle any other exceptions
#     print(f"An unexpected error occurred: {e}")


# 4. Use the finally clause for cleanup operations
# Your code here:
# Example:
# try:
#     file = open("sample.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("Error: The file does not exist")
# finally:
#     # This block always executes, regardless of whether an exception occurred
#     print("Cleanup operations...")
#     # Close the file if it was successfully opened
#     if 'file' in locals() and not file.closed:
#         file.close()
#         print("File closed")


# 5. Create and raise custom exceptions
# Your code here:
# Example:
# class InsufficientFundsError(Exception):
#     """Exception raised when a withdrawal exceeds the available balance."""
#     def __init__(self, balance, amount):
#         self.balance = balance
#         self.amount = amount
#         self.message = f"Cannot withdraw ${amount}. Balance is ${balance}."
#         super().__init__(self.message)
# 
# def withdraw(balance, amount):
#     if amount > balance:
#         raise InsufficientFundsError(balance, amount)
#     return balance - amount
# 
# try:
#     current_balance = 100
#     withdrawal_amount = 150
#     new_balance = withdraw(current_balance, withdrawal_amount)
#     print(f"New balance: ${new_balance}")
# except InsufficientFundsError as e:
#     print(f"Error: {e}")


# 6. Implement error logging
# Your code here:
# Example:
# import logging
# 
# # Configure logging
# logging.basicConfig(
#     filename='app.log',
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )
# 
# def divide(a, b):
#     try:
#         result = a / b
#         logging.info(f"Division successful: {a} / {b} = {result}")
#         return result
#     except ZeroDivisionError:
#         logging.error(f"Division by zero attempted: {a} / {b}")
#         raise
# 
# try:
#     print(divide(10, 2))
#     print(divide(10, 0))
# except ZeroDivisionError:
#     print("Cannot divide by zero")


# 7. Use assertions for debugging and validation
# Your code here:
# Example:
# def calculate_rectangle_area(length, width):
#     # Assertions to validate input
#     assert length > 0, "Length must be positive"
#     assert width > 0, "Width must be positive"
#     
#     area = length * width
#     return area
# 
# # Valid input
# try:
#     area1 = calculate_rectangle_area(5, 10)
#     print(f"Area of rectangle: {area1}")
# 
#     # Invalid input (will raise AssertionError)
#     area2 = calculate_rectangle_area(-5, 10)
#     print(f"Area of rectangle: {area2}")
# except AssertionError as e:
#     print(f"Validation error: {e}")


# Real-World Task: Form Data Validator
# This task will help you apply error handling concepts in a practical context.

# Import necessary modules
import re
import logging
import os
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='validation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Custom exception classes
class ValidationError(Exception):
    """Base class for all validation errors."""
    pass

class NameError(ValidationError):
    """Exception raised for errors in name validation."""
    pass

class EmailFormatError(ValidationError):
    """Exception raised for errors in email format."""
    pass

class PhoneFormatError(ValidationError):
    """Exception raised for errors in phone number format."""
    pass

class PasswordError(ValidationError):
    """Exception raised for errors in password validation."""
    pass

class RangeError(ValidationError):
    """Exception raised when a numeric value is out of acceptable range."""
    pass

class DateFormatError(ValidationError):
    """Exception raised for errors in date format or validity."""
    pass

class FileValidationError(ValidationError):
    """Exception raised for errors in file validation."""
    pass

# Validator class
class FormValidator:
    """A class to validate different types of form data."""
    
    def __init__(self):
        """Initialize the validator with default settings."""
        # Set up allowed file types
        self.allowed_file_types = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.txt']
        # Set up maximum file size (in MB)
        self.max_file_size = 10
        # Initialize log file
        self.setup_logging()
    
    def setup_logging(self):
        """Set up logging for validation errors."""
        # Your code here:
        pass
    
    def validate_name(self, name):
        """
        Validate that a name contains only letters and spaces.
        
        Args:
            name (str): The name to validate
            
        Returns:
            bool: True if valid
            
        Raises:
            NameError: If the name is invalid
        """
        # Your code here:
        # 1. Check if name is a string
        # 2. Check if name contains only letters and spaces
        # 3. Check if name is not empty
        # 4. Log validation result
        # 5. Raise NameError if invalid
        pass
    
    def validate_email(self, email):
        """
        Validate that an email address has the correct format.
        
        Args:
            email (str): The email to validate
            
        Returns:
            bool: True if valid
            
        Raises:
            EmailFormatError: If the email format is invalid
        """
        # Your code here:
        # 1. Check if email is a string
        # 2. Use regex to validate email format
        # 3. Log validation result
        # 4. Raise EmailFormatError if invalid
        pass
    
    def validate_phone(self, phone):
        """
        Validate that a phone number matches the expected pattern.
        
        Args:
            phone (str): The phone number to validate
            
        Returns:
            bool: True if valid
            
        Raises:
            PhoneFormatError: If the phone format is invalid
        """
        # Your code here:
        # 1. Check if phone is a string
        # 2. Use regex to validate phone format (e.g., XXX-XXX-XXXX)
        # 3. Log validation result
        # 4. Raise PhoneFormatError if invalid
        pass
    
    def validate_password(self, password):
        """
        Validate that a password meets security requirements.
        
        Args:
            password (str): The password to validate
            
        Returns:
            bool: True if valid
            
        Raises:
            PasswordError: If the password doesn't meet requirements
        """
        # Your code here:
        # 1. Check if password is a string
        # 2. Check password length (e.g., at least 8 characters)
        # 3. Check password complexity (e.g., contains letters, numbers, special chars)
        # 4. Log validation result
        # 5. Raise PasswordError with specific message if invalid
        pass
    
    def validate_age(self, age):
        """
        Validate that an age is within an acceptable range.
        
        Args:
            age (int or str): The age to validate
            
        Returns:
            bool: True if valid
            
        Raises:
            ValueError: If age cannot be converted to an integer
            RangeError: If age is outside the acceptable range
        """
        # Your code here:
        # 1. Convert age to integer if it's a string
        # 2. Check if age is within acceptable range (e.g., 0-120)
        # 3. Log validation result
        # 4. Raise appropriate exception if invalid
        pass
    
    def validate_date(self, date_str, format_str="%Y-%m-%d"):
        """
        Validate that a date string is in the correct format and is a valid date.
        
        Args:
            date_str (str): The date string to validate
            format_str (str): The expected date format
            
        Returns:
            bool: True if valid
            
        Raises:
            DateFormatError: If the date format is invalid or the date is impossible
        """
        # Your code here:
        # 1. Try to parse the date string using the specified format
        # 2. Check if the date is valid (e.g., not in the future for birth dates)
        # 3. Log validation result
        # 4. Raise DateFormatError if invalid
        pass
    
    def validate_file(self, filename, filesize_mb):
        """
        Validate that a file meets the size and type requirements.
        
        Args:
            filename (str): The name of the file
            filesize_mb (float): The size of the file in MB
            
        Returns:
            bool: True if valid
            
        Raises:
            FileValidationError: If the file doesn't meet requirements
        """
        # Your code here:
        # 1. Check file extension against allowed types
        # 2. Check file size against maximum allowed size
        # 3. Log validation result
        # 4. Raise FileValidationError if invalid
        pass
    
    def cleanup_resources(self):
        """Clean up any resources used during validation."""
        # Your code here:
        # Use a try-finally block to ensure cleanup happens
        pass

# Function to test the validator with sample data
def test_validator():
    """Test the form validator with sample valid and invalid data."""
    validator = FormValidator()
    
    print("FORM DATA VALIDATOR")
    print("==================\n")
    
    # Test valid data
    print("Testing valid data:")
    try:
        validator.validate_name("John Smith")
        print("Name 'John Smith': Valid")
        
        validator.validate_email("john@example.com")
        print("Email 'john@example.com': Valid")
        
        validator.validate_phone("555-123-4567")
        print("Phone '555-123-4567': Valid")
        
        validator.validate_password("Secure123!")
        print("Password 'Secure123!': Valid")
        
        validator.validate_age(25)
        print("Age 25: Valid")
        
        validator.validate_date("1998-05-15")
        print("Birth date '1998-05-15': Valid")
        
        validator.validate_file("document.pdf", 2.5)
        print("File 'document.pdf' (2.5MB): Valid")
    except ValidationError as e:
        print(f"Unexpected validation error: {e}")
    
    # Test invalid data
    print("\nTesting invalid data:")
    test_invalid_data(validator, "validate_name", "123", "Name '123'")
    test_invalid_data(validator, "validate_email", "not-an-email", "Email 'not-an-email'")
    test_invalid_data(validator, "validate_phone", "12345", "Phone '12345'")
    test_invalid_data(validator, "validate_password", "short", "Password 'short'")
    test_invalid_data(validator, "validate_age", 200, "Age 200")
    test_invalid_data(validator, "validate_date", "2025-13-45", "Birth date '2025-13-45'")
    test_invalid_data(validator, "validate_file", ("malware.exe", 50), "File 'malware.exe' (50MB)")
    
    print("\nValidation log saved to 'validation.log'")

def test_invalid_data(validator, method_name, data, description):
    """Test invalid data and catch the expected validation error."""
    try:
        # Handle the special case for validate_file which takes two arguments
        if method_name == "validate_file" and isinstance(data, tuple):
            getattr(validator, method_name)(data[0], data[1])
        else:
            getattr(validator, method_name)(data)
        print(f"{description}: Unexpectedly Valid")
    except ValidationError as e:
        print(f"{description}: Invalid - {e.__class__.__name__}: {e}")
    except Exception as e:
        print(f"{description}: Unexpected error: {e.__class__.__name__}: {e}")

# Main function
def main():
    """Run the form data validator."""
    try:
        test_validator()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logging.error(f"Unexpected error in main: {e}")
    finally:
        print("\nValidator test completed.")

# Uncomment the line below to run the validator test
# if __name__ == "__main__":
#     main()
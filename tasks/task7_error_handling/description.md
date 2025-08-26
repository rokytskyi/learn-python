# Task 7: Error Handling

## Objective
Learn how to handle errors and exceptions in Python to make your programs more robust and user-friendly.

## Instructions
1. Understand different types of errors (syntax, runtime, logical)
2. Use try-except blocks to catch and handle exceptions
3. Handle multiple exception types
4. Use the finally clause for cleanup operations
5. Create and raise custom exceptions
6. Implement error logging
7. Use assertions for debugging and validation

## Concepts to Learn
- Common Python exceptions (ValueError, TypeError, IndexError, KeyError, FileNotFoundError, etc.)
- Try-except-else-finally blocks
- Catching multiple exceptions
- Exception hierarchies
- Creating custom exceptions
- The `raise` statement
- Error logging with the `logging` module
- Assertions with the `assert` statement
- Debugging techniques

## Expected Output
```
Basic exception handling:
[Output showing try-except blocks in action]

Multiple exception handling:
[Output showing handling of different exception types]

Finally clause:
[Output demonstrating the finally clause]

Custom exceptions:
[Output showing custom exception creation and handling]

Error logging:
[Output showing logging of exceptions]

Assertions:
[Output demonstrating assertion usage]
```

## Real-World Task: Form Data Validator

Create a robust form data validation system that validates user input for a web form or application. This task will help you apply error handling concepts in a practical context that can be verified.

### Requirements:
1. Create a validation system that can validate the following types of data:
   - Personal information (name, email, phone number)
   - Account credentials (username, password)
   - Numeric data (age, zip code, credit card number)
   - Dates (birth date, expiration date)
   - File uploads (file type, size, name)

2. Implement the following validation features:
   - Use try-except blocks to catch and handle validation errors
   - Create custom exception classes for different types of validation errors
   - Implement proper error messages that explain what went wrong
   - Use a logging system to record validation errors
   - Implement a cleanup mechanism using finally blocks
   - Use assertions to verify internal validation logic
   - Handle multiple error types with appropriate exception handling

3. The system should validate that:
   - Names contain only valid characters and are properly formatted
   - Email addresses follow the correct format
   - Phone numbers match the expected pattern
   - Passwords meet security requirements (length, complexity)
   - Numeric values are within acceptable ranges
   - Dates are valid and in the correct format
   - Files meet size and type requirements

### Verification Criteria:
Your validation system should:
- Successfully validate correct input data
- Properly catch and handle invalid input with appropriate error messages
- Use custom exceptions for different validation errors
- Log validation errors with appropriate details
- Clean up resources properly using finally blocks
- Handle multiple types of errors gracefully
- Provide clear feedback about what went wrong and how to fix it
- Use assertions to verify internal validation logic
- Be well-organized and maintainable

### Example Output:
```
FORM DATA VALIDATOR
==================

Testing valid data:
Name 'John Smith': Valid
Email 'john@example.com': Valid
Phone '555-123-4567': Valid
Password 'Secure123!': Valid
Age 25: Valid
Birth date '1998-05-15': Valid
File 'document.pdf' (2.5MB): Valid

Testing invalid data:
Name '123': Invalid - ValidationError: Name must contain only letters and spaces
Email 'not-an-email': Invalid - EmailFormatError: Invalid email format
Phone '12345': Invalid - PhoneFormatError: Phone number must be in format XXX-XXX-XXXX
Password 'short': Invalid - PasswordError: Password must be at least 8 characters long
Age 200: Invalid - RangeError: Age must be between 0 and 120
Birth date '2025-13-45': Invalid - DateFormatError: Invalid date format or impossible date
File 'malware.exe' (50MB): Invalid - FileValidationError: File type not allowed

Validation log saved to 'validation.log'
```

## Tips
- Use specific exception types rather than catching all exceptions
- The `except` block should handle the error gracefully
- The `else` block runs when no exception occurs
- The `finally` block always runs, regardless of whether an exception occurred
- Custom exceptions should inherit from `Exception` or a more specific exception class
- Use meaningful error messages to help with debugging
- The `logging` module is more flexible than print statements for error reporting
- Assertions are useful during development but should not be relied upon in production code
- Remember that preventing errors is better than handling them
- Use context managers (`with` statement) to automatically handle cleanup operations
- Regular expressions are useful for validating patterns like email addresses and phone numbers
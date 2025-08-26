"""
Basic Arithmetic Operations Module

This module provides basic arithmetic operations like addition, subtraction,
multiplication, and division.

Functions:
    add(a, b): Returns the sum of a and b
    subtract(a, b): Returns the difference of a and b
    multiply(a, b): Returns the product of a and b
    divide(a, b): Returns the quotient of a and b
    modulo(a, b): Returns the remainder of a divided by b
    power(a, b): Returns a raised to the power of b
    floor_divide(a, b): Returns the floor division of a by b
"""

def add(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a (number): The first number
        b (number): The second number
        
    Returns:
        number: The sum of a and b
        
    Examples:
        >>> add(5, 3)
        8
        >>> add(-1, 1)
        0
    """
    # Your code here:
    pass

def subtract(a, b):
    """
    Subtract b from a and return the result.
    
    Args:
        a (number): The number to subtract from
        b (number): The number to subtract
        
    Returns:
        number: The difference of a and b
        
    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(1, 5)
        -4
    """
    # Your code here:
    pass

def multiply(a, b):
    """
    Multiply two numbers and return the result.
    
    Args:
        a (number): The first number
        b (number): The second number
        
    Returns:
        number: The product of a and b
        
    Examples:
        >>> multiply(5, 3)
        15
        >>> multiply(-2, 4)
        -8
    """
    # Your code here:
    pass

def divide(a, b):
    """
    Divide a by b and return the result.
    
    Args:
        a (number): The dividend
        b (number): The divisor
        
    Returns:
        float: The quotient of a and b
        None: If b is zero
        
    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
    """
    # Your code here:
    # Remember to handle division by zero
    pass

def modulo(a, b):
    """
    Return the remainder of a divided by b.
    
    Args:
        a (number): The dividend
        b (number): The divisor
        
    Returns:
        number: The remainder of a divided by b
        None: If b is zero
        
    Examples:
        >>> modulo(10, 3)
        1
        >>> modulo(7, 2)
        1
    """
    # Your code here:
    # Remember to handle division by zero
    pass

def power(a, b):
    """
    Return a raised to the power of b.
    
    Args:
        a (number): The base
        b (number): The exponent
        
    Returns:
        number: a raised to the power of b
        
    Examples:
        >>> power(2, 3)
        8
        >>> power(5, 2)
        25
    """
    # Your code here:
    pass

def floor_divide(a, b):
    """
    Return the floor division of a by b.
    
    Args:
        a (number): The dividend
        b (number): The divisor
        
    Returns:
        int: The floor division of a by b
        None: If b is zero
        
    Examples:
        >>> floor_divide(10, 3)
        3
        >>> floor_divide(7, 2)
        3
    """
    # Your code here:
    # Remember to handle division by zero
    pass

# Test the functions if this module is run directly
if __name__ == "__main__":
    print("Testing basic arithmetic operations:")
    
    # Test addition
    print(f"5 + 3 = {add(5, 3)}")
    
    # Test subtraction
    print(f"5 - 3 = {subtract(5, 3)}")
    
    # Test multiplication
    print(f"5 * 3 = {multiply(5, 3)}")
    
    # Test division
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"Division by zero: {divide(5, 0)}")
    
    # Test modulo
    print(f"10 % 3 = {modulo(10, 3)}")
    
    # Test power
    print(f"2 ^ 3 = {power(2, 3)}")
    
    # Test floor division
    print(f"10 // 3 = {floor_divide(10, 3)}")
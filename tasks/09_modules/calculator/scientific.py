"""
Scientific Operations Module

This module provides scientific mathematical operations like trigonometric functions,
logarithms, square roots, and other advanced mathematical operations.

Functions:
    sqrt(x): Returns the square root of x
    power(base, exponent): Returns base raised to the power of exponent
    sin(x): Returns the sine of x (x in radians)
    cos(x): Returns the cosine of x (x in radians)
    tan(x): Returns the tangent of x (x in radians)
    log(x, base): Returns the logarithm of x to the given base
    ln(x): Returns the natural logarithm of x
    factorial(n): Returns the factorial of n
"""

import math

def sqrt(x):
    """
    Calculate the square root of a number.
    
    Args:
        x (float): The number to calculate the square root of
        
    Returns:
        float: The square root of x
        None: If x is negative
        
    Examples:
        >>> sqrt(9)
        3.0
        >>> sqrt(2)
        1.4142135623730951
    """
    # Your code here:
    # Remember to handle negative numbers
    pass

def power(base, exponent):
    """
    Calculate base raised to the power of exponent.
    
    Args:
        base (float): The base number
        exponent (float): The exponent
        
    Returns:
        float: base raised to the power of exponent
        
    Examples:
        >>> power(2, 3)
        8.0
        >>> power(2, 0.5)  # Square root of 2
        1.4142135623730951
    """
    # Your code here:
    pass

def sin(x):
    """
    Calculate the sine of an angle in radians.
    
    Args:
        x (float): The angle in radians
        
    Returns:
        float: The sine of x
        
    Examples:
        >>> sin(0)
        0.0
        >>> sin(math.pi/2)  # sin(90 degrees)
        1.0
    """
    # Your code here:
    pass

def cos(x):
    """
    Calculate the cosine of an angle in radians.
    
    Args:
        x (float): The angle in radians
        
    Returns:
        float: The cosine of x
        
    Examples:
        >>> cos(0)
        1.0
        >>> cos(math.pi)  # cos(180 degrees)
        -1.0
    """
    # Your code here:
    pass

def tan(x):
    """
    Calculate the tangent of an angle in radians.
    
    Args:
        x (float): The angle in radians
        
    Returns:
        float: The tangent of x
        None: If x is a multiple of pi/2 (where tangent is undefined)
        
    Examples:
        >>> tan(0)
        0.0
        >>> tan(math.pi/4)  # tan(45 degrees)
        0.9999999999999999  # Close to 1 due to floating-point precision
    """
    # Your code here:
    # Remember to handle cases where tangent is undefined
    pass

def log(x, base=10):
    """
    Calculate the logarithm of x to the given base.
    
    Args:
        x (float): The number to calculate the logarithm of
        base (float, optional): The base of the logarithm. Defaults to 10.
        
    Returns:
        float: The logarithm of x to the given base
        None: If x <= 0 or base <= 0 or base == 1
        
    Examples:
        >>> log(100)  # Base 10 logarithm
        2.0
        >>> log(8, 2)  # Base 2 logarithm
        3.0
    """
    # Your code here:
    # Remember to handle invalid inputs (x <= 0, base <= 0, base == 1)
    pass

def ln(x):
    """
    Calculate the natural logarithm (base e) of x.
    
    Args:
        x (float): The number to calculate the natural logarithm of
        
    Returns:
        float: The natural logarithm of x
        None: If x <= 0
        
    Examples:
        >>> ln(math.e)
        1.0
        >>> ln(1)
        0.0
    """
    # Your code here:
    # Remember to handle invalid inputs (x <= 0)
    pass

def factorial(n):
    """
    Calculate the factorial of n.
    
    Args:
        n (int): The number to calculate the factorial of
        
    Returns:
        int: The factorial of n
        None: If n < 0
        
    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    # Your code here:
    # Remember to handle invalid inputs (n < 0)
    pass

# Test the functions if this module is run directly
if __name__ == "__main__":
    print("Testing scientific operations:")
    
    # Test square root
    print(f"sqrt(9) = {sqrt(9)}")
    print(f"sqrt(2) = {sqrt(2)}")
    
    # Test power
    print(f"2^3 = {power(2, 3)}")
    print(f"2^0.5 = {power(2, 0.5)}")
    
    # Test trigonometric functions
    print(f"sin(0) = {sin(0)}")
    print(f"sin(π/2) = {sin(math.pi/2)}")
    
    print(f"cos(0) = {cos(0)}")
    print(f"cos(π) = {cos(math.pi)}")
    
    print(f"tan(0) = {tan(0)}")
    print(f"tan(π/4) = {tan(math.pi/4)}")
    
    # Test logarithms
    print(f"log(100) = {log(100)}")
    print(f"log(8, 2) = {log(8, 2)}")
    print(f"ln(e) = {ln(math.e)}")
    
    # Test factorial
    print(f"5! = {factorial(5)}")
    print(f"0! = {factorial(0)}")
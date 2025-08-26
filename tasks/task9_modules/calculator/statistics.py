"""
Statistical Operations Module

This module provides statistical operations for analyzing data sets, including
measures of central tendency (mean, median, mode) and measures of dispersion
(variance, standard deviation, range).

Functions:
    mean(data): Returns the arithmetic mean of the data
    median(data): Returns the median of the data
    mode(data): Returns the mode(s) of the data
    variance(data): Returns the variance of the data
    std_dev(data): Returns the standard deviation of the data
    range_value(data): Returns the range of the data
    quartiles(data): Returns the quartiles of the data
    correlation(data1, data2): Returns the correlation coefficient between two data sets
"""

import math
from collections import Counter

def mean(data):
    """
    Calculate the arithmetic mean of a data set.
    
    Args:
        data (list): A list of numbers
        
    Returns:
        float: The arithmetic mean of the data
        None: If the data list is empty
        
    Examples:
        >>> mean([1, 2, 3, 4, 5])
        3.0
        >>> mean([10, 20, 30, 40])
        25.0
    """
    # Your code here:
    # Remember to handle empty lists
    pass

def median(data):
    """
    Calculate the median of a data set.
    
    Args:
        data (list): A list of numbers
        
    Returns:
        float: The median of the data
        None: If the data list is empty
        
    Examples:
        >>> median([1, 3, 5, 7, 9])
        5
        >>> median([1, 3, 5, 7])
        4.0
    """
    # Your code here:
    # Remember to handle empty lists
    # Remember to handle both odd and even length lists
    pass

def mode(data):
    """
    Find the mode(s) of a data set.
    
    Args:
        data (list): A list of values
        
    Returns:
        list: A list of the most common value(s) in the data
        None: If the data list is empty
        
    Examples:
        >>> mode([1, 2, 2, 3, 3, 3, 4])
        [3]
        >>> mode([1, 1, 2, 2, 3])
        [1, 2]
    """
    # Your code here:
    # Remember to handle empty lists
    # Remember to handle multiple modes
    pass

def variance(data):
    """
    Calculate the variance of a data set.
    
    Args:
        data (list): A list of numbers
        
    Returns:
        float: The variance of the data
        None: If the data list is empty or has only one element
        
    Examples:
        >>> variance([1, 2, 3, 4, 5])
        2.0
        >>> variance([10, 20, 30, 40])
        125.0
    """
    # Your code here:
    # Remember to handle empty lists and lists with only one element
    pass

def std_dev(data):
    """
    Calculate the standard deviation of a data set.
    
    Args:
        data (list): A list of numbers
        
    Returns:
        float: The standard deviation of the data
        None: If the data list is empty or has only one element
        
    Examples:
        >>> std_dev([1, 2, 3, 4, 5])
        1.4142135623730951
        >>> std_dev([10, 20, 30, 40])
        11.180339887498949
    """
    # Your code here:
    # Remember to handle empty lists and lists with only one element
    # Hint: Use the variance function
    pass

def range_value(data):
    """
    Calculate the range of a data set.
    
    Args:
        data (list): A list of numbers
        
    Returns:
        float: The range of the data (max - min)
        None: If the data list is empty
        
    Examples:
        >>> range_value([1, 2, 3, 4, 5])
        4
        >>> range_value([10, 20, 30, 40])
        30
    """
    # Your code here:
    # Remember to handle empty lists
    pass

def quartiles(data):
    """
    Calculate the quartiles of a data set.
    
    Args:
        data (list): A list of numbers
        
    Returns:
        tuple: A tuple containing the first quartile (Q1), second quartile (Q2, median),
               and third quartile (Q3)
        None: If the data list is empty
        
    Examples:
        >>> quartiles([1, 2, 3, 4, 5, 6, 7, 8, 9])
        (3, 5, 7)
        >>> quartiles([1, 2, 3, 4, 5, 6, 7, 8])
        (2.5, 4.5, 6.5)
    """
    # Your code here:
    # Remember to handle empty lists
    # Hint: Use the median function
    pass

def correlation(data1, data2):
    """
    Calculate the Pearson correlation coefficient between two data sets.
    
    Args:
        data1 (list): The first data set
        data2 (list): The second data set
        
    Returns:
        float: The correlation coefficient between the two data sets
        None: If either data list is empty or the lists have different lengths
              or if the standard deviation of either data set is zero
        
    Examples:
        >>> correlation([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
        -1.0
        >>> correlation([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
        1.0
    """
    # Your code here:
    # Remember to handle empty lists, lists with different lengths,
    # and lists with zero standard deviation
    pass

# Test the functions if this module is run directly
if __name__ == "__main__":
    print("Testing statistical operations:")
    
    # Sample data sets
    data1 = [1, 2, 3, 4, 5]
    data2 = [5, 4, 3, 2, 1]
    data3 = [1, 2, 2, 3, 3, 3, 4, 4, 5]
    
    # Test mean
    print(f"Mean of {data1} = {mean(data1)}")
    
    # Test median
    print(f"Median of {data1} = {median(data1)}")
    print(f"Median of {data3} = {median(data3)}")
    
    # Test mode
    print(f"Mode of {data3} = {mode(data3)}")
    
    # Test variance and standard deviation
    print(f"Variance of {data1} = {variance(data1)}")
    print(f"Standard deviation of {data1} = {std_dev(data1)}")
    
    # Test range
    print(f"Range of {data1} = {range_value(data1)}")
    
    # Test quartiles
    print(f"Quartiles of {data1} = {quartiles(data1)}")
    
    # Test correlation
    print(f"Correlation between {data1} and {data2} = {correlation(data1, data2)}")
    print(f"Correlation between {data1} and {data1} = {correlation(data1, data1)}")
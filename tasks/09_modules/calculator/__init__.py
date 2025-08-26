"""
Scientific Calculator Package

This package provides various mathematical and scientific calculation functions
organized into separate modules for different types of operations.

Modules:
- basic: Basic arithmetic operations
- scientific: Scientific operations (trigonometry, logarithms, etc.)
- statistics: Statistical operations (mean, median, etc.)
- conversions: Unit conversion functions
- financial: Financial calculations

Usage:
    import calculator
    result = calculator.add(5, 3)  # Basic operation exposed at package level
    
    from calculator import scientific
    sin_value = scientific.sin(0.5)
"""

# Package version information
__version__ = "0.1.0"
__author__ = "Your Name"

# Import and expose key functions at the package level for easy access
# These will be available directly from the calculator package

# From basic module
try:
    from .basic import add, subtract, multiply, divide
except ImportError:
    # Placeholder functions if the module hasn't been implemented yet
    def add(a, b): return a + b
    def subtract(a, b): return a - b
    def multiply(a, b): return a * b
    def divide(a, b): return a / b if b != 0 else None

# From scientific module
try:
    from .scientific import sqrt, power, sin, cos
except ImportError:
    # These will be defined when you implement the scientific module
    pass

# From statistics module
try:
    from .statistics import mean, median
except ImportError:
    # These will be defined when you implement the statistics module
    pass

# List of all modules in this package
__all__ = ['basic', 'scientific', 'statistics', 'conversions', 'financial']
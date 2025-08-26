"""
Financial Calculations Module

This module provides functions for various financial calculations, including
compound interest, loan payments, investment growth, and depreciation.

Functions:
    simple_interest(principal, rate, time): Calculate simple interest
    compound_interest(principal, rate, time, compounds_per_year): Calculate compound interest
    future_value(principal, rate, time, compounds_per_year): Calculate future value of an investment
    loan_payment(principal, rate, time): Calculate monthly loan payment
    loan_payoff_time(principal, rate, payment): Calculate time to pay off a loan
    depreciation_linear(initial_value, salvage_value, useful_life): Calculate linear depreciation
    depreciation_reducing_balance(initial_value, rate, time): Calculate reducing balance depreciation
    roi(gain, cost): Calculate return on investment
    break_even(fixed_costs, variable_cost_per_unit, price_per_unit): Calculate break-even point
"""

import math

def simple_interest(principal, rate, time):
    """
    Calculate simple interest.
    
    Args:
        principal (float): The initial amount of money
        rate (float): The interest rate (as a decimal, e.g., 0.05 for 5%)
        time (float): The time period in years
        
    Returns:
        float: The simple interest earned
        
    Examples:
        >>> simple_interest(1000, 0.05, 1)
        50.0
        >>> simple_interest(1000, 0.05, 3)
        150.0
    """
    # Your code here:
    pass

def compound_interest(principal, rate, time, compounds_per_year=1):
    """
    Calculate compound interest.
    
    Args:
        principal (float): The initial amount of money
        rate (float): The annual interest rate (as a decimal, e.g., 0.05 for 5%)
        time (float): The time period in years
        compounds_per_year (int, optional): Number of times interest is compounded per year.
                                           Defaults to 1 (annually).
        
    Returns:
        float: The compound interest earned
        
    Examples:
        >>> compound_interest(1000, 0.05, 1)  # Annual compounding
        50.0
        >>> compound_interest(1000, 0.05, 1, 12)  # Monthly compounding
        51.16
    """
    # Your code here:
    pass

def future_value(principal, rate, time, compounds_per_year=1):
    """
    Calculate the future value of an investment with compound interest.
    
    Args:
        principal (float): The initial amount of money
        rate (float): The annual interest rate (as a decimal, e.g., 0.05 for 5%)
        time (float): The time period in years
        compounds_per_year (int, optional): Number of times interest is compounded per year.
                                           Defaults to 1 (annually).
        
    Returns:
        float: The future value of the investment
        
    Examples:
        >>> future_value(1000, 0.05, 1)  # Annual compounding
        1050.0
        >>> future_value(1000, 0.05, 10)  # 10 years of annual compounding
        1628.89
    """
    # Your code here:
    pass

def loan_payment(principal, rate, time):
    """
    Calculate the monthly payment for a loan.
    
    Args:
        principal (float): The loan amount
        rate (float): The annual interest rate (as a decimal, e.g., 0.05 for 5%)
        time (float): The loan term in years
        
    Returns:
        float: The monthly payment amount
        
    Examples:
        >>> loan_payment(100000, 0.05, 30)  # 30-year mortgage at 5%
        536.82
        >>> loan_payment(20000, 0.06, 5)  # 5-year car loan at 6%
        386.66
    """
    # Your code here:
    # Use the formula: P = (r*PV) / (1 - (1+r)^-n)
    # where P is the payment, PV is the present value (principal),
    # r is the rate per period, and n is the number of periods
    pass

def loan_payoff_time(principal, rate, payment):
    """
    Calculate the time (in years) to pay off a loan with fixed monthly payments.
    
    Args:
        principal (float): The loan amount
        rate (float): The annual interest rate (as a decimal, e.g., 0.05 for 5%)
        payment (float): The monthly payment amount
        
    Returns:
        float: The time to pay off the loan in years
        None: If the payment is too small to ever pay off the loan
        
    Examples:
        >>> loan_payoff_time(100000, 0.05, 536.82)  # Payment for 30-year mortgage
        30.0
        >>> loan_payoff_time(20000, 0.06, 400)  # Slightly higher payment than minimum
        4.85
    """
    # Your code here:
    # Use the formula: n = -log(1 - (r*PV)/P) / log(1+r)
    # where n is the number of periods, PV is the present value (principal),
    # r is the rate per period, and P is the payment
    # Remember to handle the case where the payment is too small
    pass

def depreciation_linear(initial_value, salvage_value, useful_life):
    """
    Calculate the annual depreciation amount using the straight-line (linear) method.
    
    Args:
        initial_value (float): The initial value of the asset
        salvage_value (float): The salvage value at the end of its useful life
        useful_life (float): The useful life of the asset in years
        
    Returns:
        float: The annual depreciation amount
        None: If useful_life is zero or negative
        
    Examples:
        >>> depreciation_linear(10000, 1000, 5)
        1800.0
        >>> depreciation_linear(50000, 5000, 10)
        4500.0
    """
    # Your code here:
    # Remember to handle invalid inputs (useful_life <= 0)
    pass

def depreciation_reducing_balance(initial_value, rate, time):
    """
    Calculate the depreciated value using the reducing balance (declining balance) method.
    
    Args:
        initial_value (float): The initial value of the asset
        rate (float): The annual depreciation rate (as a decimal, e.g., 0.2 for 20%)
        time (float): The time period in years
        
    Returns:
        float: The depreciated value after the specified time
        None: If rate is not between 0 and 1
        
    Examples:
        >>> depreciation_reducing_balance(10000, 0.2, 1)  # After 1 year
        8000.0
        >>> depreciation_reducing_balance(10000, 0.2, 5)  # After 5 years
        3277.0
    """
    # Your code here:
    # Remember to handle invalid inputs (rate < 0 or rate > 1)
    pass

def roi(gain, cost):
    """
    Calculate the Return on Investment (ROI).
    
    Args:
        gain (float): The gain from the investment
        cost (float): The cost of the investment
        
    Returns:
        float: The ROI as a decimal (multiply by 100 for percentage)
        None: If cost is zero
        
    Examples:
        >>> roi(1500, 1000)  # $500 profit on $1000 investment
        0.5
        >>> roi(800, 1000)  # $200 loss on $1000 investment
        -0.2
    """
    # Your code here:
    # Remember to handle division by zero
    pass

def break_even(fixed_costs, variable_cost_per_unit, price_per_unit):
    """
    Calculate the break-even point (number of units).
    
    Args:
        fixed_costs (float): The total fixed costs
        variable_cost_per_unit (float): The variable cost per unit
        price_per_unit (float): The selling price per unit
        
    Returns:
        float: The break-even point in number of units
        None: If price_per_unit <= variable_cost_per_unit
        
    Examples:
        >>> break_even(10000, 5, 15)  # $10000 fixed costs, $5 variable cost, $15 price
        1000.0
        >>> break_even(20000, 10, 20)
        2000.0
    """
    # Your code here:
    # Remember to handle the case where price <= variable cost
    pass

# Test the functions if this module is run directly
if __name__ == "__main__":
    print("Testing financial calculations:")
    
    # Test simple and compound interest
    print("\nInterest calculations:")
    print(f"Simple interest on $1000 at 5% for 1 year: ${simple_interest(1000, 0.05, 1):.2f}")
    print(f"Compound interest on $1000 at 5% for 1 year (annual): ${compound_interest(1000, 0.05, 1):.2f}")
    print(f"Compound interest on $1000 at 5% for 1 year (monthly): ${compound_interest(1000, 0.05, 1, 12):.2f}")
    
    # Test future value
    print("\nFuture value calculations:")
    print(f"Future value of $1000 at 5% for 10 years: ${future_value(1000, 0.05, 10):.2f}")
    
    # Test loan calculations
    print("\nLoan calculations:")
    print(f"Monthly payment on $100,000 loan at 5% for 30 years: ${loan_payment(100000, 0.05, 30):.2f}")
    print(f"Time to pay off $20,000 loan at 6% with $400 monthly payment: {loan_payoff_time(20000, 0.06, 400):.2f} years")
    
    # Test depreciation
    print("\nDepreciation calculations:")
    print(f"Annual linear depreciation on $10,000 asset with $1,000 salvage over 5 years: ${depreciation_linear(10000, 1000, 5):.2f}")
    print(f"Value after 5 years of 20% reducing balance depreciation on $10,000 asset: ${depreciation_reducing_balance(10000, 0.2, 5):.2f}")
    
    # Test ROI and break-even
    print("\nROI and break-even calculations:")
    print(f"ROI on $1000 investment with $1500 return: {roi(1500, 1000):.2f} ({roi(1500, 1000)*100:.0f}%)")
    print(f"Break-even point with $10,000 fixed costs, $5 variable cost, $15 price: {break_even(10000, 5, 15):.0f} units")
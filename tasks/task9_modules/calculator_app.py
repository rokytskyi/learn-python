#!/usr/bin/env python3
"""
Scientific Calculator Application

This script provides a command-line interface for the calculator package,
demonstrating different import techniques and package usage.

Usage:
    python calculator_app.py

The application allows users to perform various calculations using the
different modules in the calculator package:
- Basic arithmetic operations
- Scientific operations
- Statistical operations
- Unit conversions
- Financial calculations
"""

# Import the entire package
import calculator

# Import specific modules with aliases
from calculator import scientific as sci
from calculator import statistics as stats
from calculator import conversions as conv
from calculator import financial as fin

# Standard library imports
import sys
import math


def display_main_menu():
    """Display the main menu options."""
    print("\nScientific Calculator")
    print("====================")
    print("1. Basic Operations")
    print("2. Scientific Operations")
    print("3. Statistical Operations")
    print("4. Unit Conversions")
    print("5. Financial Calculations")
    print("6. Exit")


def display_basic_menu():
    """Display the basic operations menu."""
    print("\nBasic Operations")
    print("---------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo")
    print("6. Power")
    print("7. Floor Division")
    print("8. Return to Main Menu")


def display_scientific_menu():
    """Display the scientific operations menu."""
    print("\nScientific Operations")
    print("--------------------")
    print("1. Square Root")
    print("2. Power")
    print("3. Sine")
    print("4. Cosine")
    print("5. Tangent")
    print("6. Logarithm")
    print("7. Natural Logarithm")
    print("8. Factorial")
    print("9. Return to Main Menu")


def display_statistics_menu():
    """Display the statistical operations menu."""
    print("\nStatistical Operations")
    print("---------------------")
    print("1. Mean")
    print("2. Median")
    print("3. Mode")
    print("4. Variance")
    print("5. Standard Deviation")
    print("6. Range")
    print("7. Quartiles")
    print("8. Correlation")
    print("9. Return to Main Menu")


def display_conversions_menu():
    """Display the unit conversions menu."""
    print("\nUnit Conversions")
    print("---------------")
    print("1. Temperature Conversions")
    print("2. Length Conversions")
    print("3. Weight/Mass Conversions")
    print("4. Volume Conversions")
    print("5. Time Conversions")
    print("6. Return to Main Menu")


def display_financial_menu():
    """Display the financial calculations menu."""
    print("\nFinancial Calculations")
    print("---------------------")
    print("1. Simple Interest")
    print("2. Compound Interest")
    print("3. Future Value")
    print("4. Loan Payment")
    print("5. Loan Payoff Time")
    print("6. Depreciation")
    print("7. Return on Investment")
    print("8. Break-Even Point")
    print("9. Return to Main Menu")


def get_number_input(prompt):
    """Get a number input from the user with error handling."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_list_input(prompt):
    """Get a list of numbers from the user with error handling."""
    while True:
        try:
            input_str = input(prompt)
            # Split the input string by commas and convert each part to a float
            return [float(x.strip()) for x in input_str.split(",")]
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")


def handle_basic_operations():
    """Handle the basic operations menu."""
    while True:
        display_basic_menu()
        choice = input("\nEnter your choice (1-8): ")
        
        if choice == "8":
            return
        
        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            a = get_number_input("Enter first number: ")
            b = get_number_input("Enter second number: ")
            
            if choice == "1":  # Addition
                result = calculator.add(a, b)
                print(f"\nResult: {a} + {b} = {result}")
            elif choice == "2":  # Subtraction
                result = calculator.subtract(a, b)
                print(f"\nResult: {a} - {b} = {result}")
            elif choice == "3":  # Multiplication
                result = calculator.multiply(a, b)
                print(f"\nResult: {a} * {b} = {result}")
            elif choice == "4":  # Division
                result = calculator.divide(a, b)
                if result is None:
                    print("\nError: Division by zero")
                else:
                    print(f"\nResult: {a} / {b} = {result}")
            elif choice == "5":  # Modulo
                # Using the basic module directly
                from calculator.basic import modulo
                result = modulo(a, b)
                if result is None:
                    print("\nError: Modulo by zero")
                else:
                    print(f"\nResult: {a} % {b} = {result}")
            elif choice == "6":  # Power
                # Using the basic module directly
                from calculator.basic import power
                result = power(a, b)
                print(f"\nResult: {a} ^ {b} = {result}")
            elif choice == "7":  # Floor Division
                # Using the basic module directly
                from calculator.basic import floor_divide
                result = floor_divide(a, b)
                if result is None:
                    print("\nError: Division by zero")
                else:
                    print(f"\nResult: {a} // {b} = {result}")
        else:
            print("\nInvalid choice. Please enter a number between 1 and 8.")


def handle_scientific_operations():
    """Handle the scientific operations menu."""
    while True:
        display_scientific_menu()
        choice = input("\nEnter your choice (1-9): ")
        
        if choice == "9":
            return
        
        if choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            if choice == "1":  # Square Root
                x = get_number_input("Enter a number: ")
                result = sci.sqrt(x)
                if result is None:
                    print("\nError: Cannot calculate square root of a negative number")
                else:
                    print(f"\nResult: sqrt({x}) = {result}")
            elif choice == "2":  # Power
                base = get_number_input("Enter base: ")
                exponent = get_number_input("Enter exponent: ")
                result = sci.power(base, exponent)
                print(f"\nResult: {base} ^ {exponent} = {result}")
            elif choice == "3":  # Sine
                angle = get_number_input("Enter angle in radians: ")
                result = sci.sin(angle)
                print(f"\nResult: sin({angle}) = {result}")
            elif choice == "4":  # Cosine
                angle = get_number_input("Enter angle in radians: ")
                result = sci.cos(angle)
                print(f"\nResult: cos({angle}) = {result}")
            elif choice == "5":  # Tangent
                angle = get_number_input("Enter angle in radians: ")
                result = sci.tan(angle)
                if result is None:
                    print("\nError: Tangent is undefined at this angle")
                else:
                    print(f"\nResult: tan({angle}) = {result}")
            elif choice == "6":  # Logarithm
                x = get_number_input("Enter a number: ")
                base = get_number_input("Enter base (default is 10): ")
                result = sci.log(x, base)
                if result is None:
                    print("\nError: Invalid input for logarithm")
                else:
                    print(f"\nResult: log_{base}({x}) = {result}")
            elif choice == "7":  # Natural Logarithm
                x = get_number_input("Enter a number: ")
                result = sci.ln(x)
                if result is None:
                    print("\nError: Cannot calculate logarithm of a non-positive number")
                else:
                    print(f"\nResult: ln({x}) = {result}")
            elif choice == "8":  # Factorial
                n = get_number_input("Enter a non-negative integer: ")
                result = sci.factorial(int(n))
                if result is None:
                    print("\nError: Cannot calculate factorial of a negative number")
                else:
                    print(f"\nResult: {int(n)}! = {result}")
        else:
            print("\nInvalid choice. Please enter a number between 1 and 9.")


def handle_statistics_operations():
    """Handle the statistical operations menu."""
    while True:
        display_statistics_menu()
        choice = input("\nEnter your choice (1-9): ")
        
        if choice == "9":
            return
        
        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            data = get_list_input("Enter data (comma-separated numbers): ")
            
            if choice == "1":  # Mean
                result = stats.mean(data)
                if result is None:
                    print("\nError: Cannot calculate mean of empty data")
                else:
                    print(f"\nResult: Mean of {data} = {result}")
            elif choice == "2":  # Median
                result = stats.median(data)
                if result is None:
                    print("\nError: Cannot calculate median of empty data")
                else:
                    print(f"\nResult: Median of {data} = {result}")
            elif choice == "3":  # Mode
                result = stats.mode(data)
                if result is None:
                    print("\nError: Cannot calculate mode of empty data")
                else:
                    print(f"\nResult: Mode of {data} = {result}")
            elif choice == "4":  # Variance
                result = stats.variance(data)
                if result is None:
                    print("\nError: Cannot calculate variance of empty data or data with only one element")
                else:
                    print(f"\nResult: Variance of {data} = {result}")
            elif choice == "5":  # Standard Deviation
                result = stats.std_dev(data)
                if result is None:
                    print("\nError: Cannot calculate standard deviation of empty data or data with only one element")
                else:
                    print(f"\nResult: Standard deviation of {data} = {result}")
            elif choice == "6":  # Range
                result = stats.range_value(data)
                if result is None:
                    print("\nError: Cannot calculate range of empty data")
                else:
                    print(f"\nResult: Range of {data} = {result}")
            elif choice == "7":  # Quartiles
                result = stats.quartiles(data)
                if result is None:
                    print("\nError: Cannot calculate quartiles of empty data")
                else:
                    print(f"\nResult: Quartiles of {data} = {result}")
        elif choice == "8":  # Correlation
            data1 = get_list_input("Enter first data set (comma-separated numbers): ")
            data2 = get_list_input("Enter second data set (comma-separated numbers): ")
            result = stats.correlation(data1, data2)
            if result is None:
                print("\nError: Cannot calculate correlation (check data sets)")
            else:
                print(f"\nResult: Correlation between {data1} and {data2} = {result}")
        else:
            print("\nInvalid choice. Please enter a number between 1 and 9.")


def handle_conversions():
    """Handle the unit conversions menu."""
    while True:
        display_conversions_menu()
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "6":
            return
        
        if choice == "1":  # Temperature Conversions
            print("\nTemperature Conversions:")
            print("1. Celsius to Fahrenheit")
            print("2. Fahrenheit to Celsius")
            print("3. Celsius to Kelvin")
            print("4. Kelvin to Celsius")
            
            temp_choice = input("\nEnter your choice (1-4): ")
            
            if temp_choice == "1":
                celsius = get_number_input("Enter temperature in Celsius: ")
                result = conv.celsius_to_fahrenheit(celsius)
                print(f"\nResult: {celsius}°C = {result}°F")
            elif temp_choice == "2":
                fahrenheit = get_number_input("Enter temperature in Fahrenheit: ")
                result = conv.fahrenheit_to_celsius(fahrenheit)
                print(f"\nResult: {fahrenheit}°F = {result}°C")
            elif temp_choice == "3":
                celsius = get_number_input("Enter temperature in Celsius: ")
                result = conv.celsius_to_kelvin(celsius)
                print(f"\nResult: {celsius}°C = {result}K")
            elif temp_choice == "4":
                kelvin = get_number_input("Enter temperature in Kelvin: ")
                result = conv.kelvin_to_celsius(kelvin)
                if result is None:
                    print("\nError: Temperature cannot be below absolute zero (0K)")
                else:
                    print(f"\nResult: {kelvin}K = {result}°C")
            else:
                print("\nInvalid choice.")
        
        elif choice == "2":  # Length Conversions
            print("\nLength Conversions:")
            print("1. Inches to Centimeters")
            print("2. Centimeters to Inches")
            print("3. Feet to Meters")
            print("4. Meters to Feet")
            print("5. Miles to Kilometers")
            print("6. Kilometers to Miles")
            
            length_choice = input("\nEnter your choice (1-6): ")
            
            if length_choice == "1":
                inches = get_number_input("Enter length in inches: ")
                result = conv.inches_to_cm(inches)
                print(f"\nResult: {inches} inches = {result} cm")
            elif length_choice == "2":
                cm = get_number_input("Enter length in centimeters: ")
                result = conv.cm_to_inches(cm)
                print(f"\nResult: {cm} cm = {result} inches")
            elif length_choice == "3":
                feet = get_number_input("Enter length in feet: ")
                result = conv.feet_to_meters(feet)
                print(f"\nResult: {feet} feet = {result} meters")
            elif length_choice == "4":
                meters = get_number_input("Enter length in meters: ")
                result = conv.meters_to_feet(meters)
                print(f"\nResult: {meters} meters = {result} feet")
            elif length_choice == "5":
                miles = get_number_input("Enter distance in miles: ")
                result = conv.miles_to_km(miles)
                print(f"\nResult: {miles} miles = {result} km")
            elif length_choice == "6":
                km = get_number_input("Enter distance in kilometers: ")
                result = conv.km_to_miles(km)
                print(f"\nResult: {km} km = {result} miles")
            else:
                print("\nInvalid choice.")
        
        elif choice in ["3", "4", "5"]:  # Other conversions
            print("\nThis feature is not fully implemented yet.")
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")


def handle_financial_calculations():
    """Handle the financial calculations menu."""
    while True:
        display_financial_menu()
        choice = input("\nEnter your choice (1-9): ")
        
        if choice == "9":
            return
        
        if choice == "1":  # Simple Interest
            principal = get_number_input("Enter principal amount: ")
            rate = get_number_input("Enter annual interest rate (as decimal, e.g., 0.05 for 5%): ")
            time = get_number_input("Enter time period in years: ")
            
            result = fin.simple_interest(principal, rate, time)
            print(f"\nResult: Simple interest on ${principal} at {rate*100}% for {time} years = ${result:.2f}")
        
        elif choice == "2":  # Compound Interest
            principal = get_number_input("Enter principal amount: ")
            rate = get_number_input("Enter annual interest rate (as decimal, e.g., 0.05 for 5%): ")
            time = get_number_input("Enter time period in years: ")
            compounds = int(get_number_input("Enter number of times interest is compounded per year: "))
            
            result = fin.compound_interest(principal, rate, time, compounds)
            print(f"\nResult: Compound interest on ${principal} at {rate*100}% for {time} years (compounded {compounds} times per year) = ${result:.2f}")
        
        elif choice in ["3", "4", "5", "6", "7", "8"]:  # Other financial calculations
            print("\nThis feature is not fully implemented yet.")
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 9.")


def main():
    """Main function to run the calculator application."""
    print("\nWelcome to the Scientific Calculator!")
    print(f"Calculator Package Version: {calculator.__version__}")
    
    while True:
        display_main_menu()
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            handle_basic_operations()
        elif choice == "2":
            handle_scientific_operations()
        elif choice == "3":
            handle_statistics_operations()
        elif choice == "4":
            handle_conversions()
        elif choice == "5":
            handle_financial_calculations()
        elif choice == "6":
            print("\nThank you for using the Scientific Calculator. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)
"""
Unit Conversions Module

This module provides functions for converting between different units of measurement,
including temperature, length, weight/mass, volume, and time.

Functions:
    Temperature conversions:
    - celsius_to_fahrenheit(celsius): Convert Celsius to Fahrenheit
    - fahrenheit_to_celsius(fahrenheit): Convert Fahrenheit to Celsius
    - celsius_to_kelvin(celsius): Convert Celsius to Kelvin
    - kelvin_to_celsius(kelvin): Convert Kelvin to Celsius
    
    Length conversions:
    - inches_to_cm(inches): Convert inches to centimeters
    - cm_to_inches(cm): Convert centimeters to inches
    - feet_to_meters(feet): Convert feet to meters
    - meters_to_feet(meters): Convert meters to feet
    - miles_to_km(miles): Convert miles to kilometers
    - km_to_miles(km): Convert kilometers to miles
    
    Weight/Mass conversions:
    - pounds_to_kg(pounds): Convert pounds to kilograms
    - kg_to_pounds(kg): Convert kilograms to pounds
    - ounces_to_grams(ounces): Convert ounces to grams
    - grams_to_ounces(grams): Convert grams to ounces
    
    Volume conversions:
    - gallons_to_liters(gallons): Convert gallons to liters
    - liters_to_gallons(liters): Convert liters to gallons
    
    Time conversions:
    - hours_to_minutes(hours): Convert hours to minutes
    - minutes_to_seconds(minutes): Convert minutes to seconds
    - days_to_hours(days): Convert days to hours
"""

# Temperature conversions
def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Fahrenheit
        
    Examples:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    # Your code here:
    pass

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
        
    Returns:
        float: Temperature in Celsius
        
    Examples:
        >>> fahrenheit_to_celsius(32)
        0.0
        >>> fahrenheit_to_celsius(212)
        100.0
    """
    # Your code here:
    pass

def celsius_to_kelvin(celsius):
    """
    Convert temperature from Celsius to Kelvin.
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Kelvin
        
    Examples:
        >>> celsius_to_kelvin(0)
        273.15
        >>> celsius_to_kelvin(100)
        373.15
    """
    # Your code here:
    pass

def kelvin_to_celsius(kelvin):
    """
    Convert temperature from Kelvin to Celsius.
    
    Args:
        kelvin (float): Temperature in Kelvin
        
    Returns:
        float: Temperature in Celsius
        None: If kelvin is less than absolute zero (0 K)
        
    Examples:
        >>> kelvin_to_celsius(273.15)
        0.0
        >>> kelvin_to_celsius(373.15)
        100.0
    """
    # Your code here:
    # Remember to handle invalid inputs (kelvin < 0)
    pass

# Length conversions
def inches_to_cm(inches):
    """
    Convert length from inches to centimeters.
    
    Args:
        inches (float): Length in inches
        
    Returns:
        float: Length in centimeters
        
    Examples:
        >>> inches_to_cm(1)
        2.54
        >>> inches_to_cm(10)
        25.4
    """
    # Your code here:
    pass

def cm_to_inches(cm):
    """
    Convert length from centimeters to inches.
    
    Args:
        cm (float): Length in centimeters
        
    Returns:
        float: Length in inches
        
    Examples:
        >>> cm_to_inches(2.54)
        1.0
        >>> cm_to_inches(25.4)
        10.0
    """
    # Your code here:
    pass

def feet_to_meters(feet):
    """
    Convert length from feet to meters.
    
    Args:
        feet (float): Length in feet
        
    Returns:
        float: Length in meters
        
    Examples:
        >>> feet_to_meters(1)
        0.3048
        >>> feet_to_meters(10)
        3.048
    """
    # Your code here:
    pass

def meters_to_feet(meters):
    """
    Convert length from meters to feet.
    
    Args:
        meters (float): Length in meters
        
    Returns:
        float: Length in feet
        
    Examples:
        >>> meters_to_feet(1)
        3.280839895013123
        >>> meters_to_feet(3)
        9.84251968503937
    """
    # Your code here:
    pass

def miles_to_km(miles):
    """
    Convert distance from miles to kilometers.
    
    Args:
        miles (float): Distance in miles
        
    Returns:
        float: Distance in kilometers
        
    Examples:
        >>> miles_to_km(1)
        1.60934
        >>> miles_to_km(10)
        16.0934
    """
    # Your code here:
    pass

def km_to_miles(km):
    """
    Convert distance from kilometers to miles.
    
    Args:
        km (float): Distance in kilometers
        
    Returns:
        float: Distance in miles
        
    Examples:
        >>> km_to_miles(1)
        0.621371
        >>> km_to_miles(10)
        6.21371
    """
    # Your code here:
    pass

# Weight/Mass conversions
def pounds_to_kg(pounds):
    """
    Convert weight from pounds to kilograms.
    
    Args:
        pounds (float): Weight in pounds
        
    Returns:
        float: Weight in kilograms
        
    Examples:
        >>> pounds_to_kg(1)
        0.45359237
        >>> pounds_to_kg(10)
        4.5359237
    """
    # Your code here:
    pass

def kg_to_pounds(kg):
    """
    Convert weight from kilograms to pounds.
    
    Args:
        kg (float): Weight in kilograms
        
    Returns:
        float: Weight in pounds
        
    Examples:
        >>> kg_to_pounds(1)
        2.2046226218487757
        >>> kg_to_pounds(5)
        11.023113109243879
    """
    # Your code here:
    pass

def ounces_to_grams(ounces):
    """
    Convert weight from ounces to grams.
    
    Args:
        ounces (float): Weight in ounces
        
    Returns:
        float: Weight in grams
        
    Examples:
        >>> ounces_to_grams(1)
        28.349523125
        >>> ounces_to_grams(16)  # 1 pound = 16 ounces
        453.59237
    """
    # Your code here:
    pass

def grams_to_ounces(grams):
    """
    Convert weight from grams to ounces.
    
    Args:
        grams (float): Weight in grams
        
    Returns:
        float: Weight in ounces
        
    Examples:
        >>> grams_to_ounces(28.349523125)
        1.0
        >>> grams_to_ounces(100)
        3.5273962
    """
    # Your code here:
    pass

# Volume conversions
def gallons_to_liters(gallons):
    """
    Convert volume from gallons to liters.
    
    Args:
        gallons (float): Volume in gallons
        
    Returns:
        float: Volume in liters
        
    Examples:
        >>> gallons_to_liters(1)
        3.78541
        >>> gallons_to_liters(10)
        37.8541
    """
    # Your code here:
    pass

def liters_to_gallons(liters):
    """
    Convert volume from liters to gallons.
    
    Args:
        liters (float): Volume in liters
        
    Returns:
        float: Volume in gallons
        
    Examples:
        >>> liters_to_gallons(3.78541)
        1.0
        >>> liters_to_gallons(10)
        2.641720523581484
    """
    # Your code here:
    pass

# Time conversions
def hours_to_minutes(hours):
    """
    Convert time from hours to minutes.
    
    Args:
        hours (float): Time in hours
        
    Returns:
        float: Time in minutes
        
    Examples:
        >>> hours_to_minutes(1)
        60.0
        >>> hours_to_minutes(2.5)
        150.0
    """
    # Your code here:
    pass

def minutes_to_seconds(minutes):
    """
    Convert time from minutes to seconds.
    
    Args:
        minutes (float): Time in minutes
        
    Returns:
        float: Time in seconds
        
    Examples:
        >>> minutes_to_seconds(1)
        60.0
        >>> minutes_to_seconds(2.5)
        150.0
    """
    # Your code here:
    pass

def days_to_hours(days):
    """
    Convert time from days to hours.
    
    Args:
        days (float): Time in days
        
    Returns:
        float: Time in hours
        
    Examples:
        >>> days_to_hours(1)
        24.0
        >>> days_to_hours(2.5)
        60.0
    """
    # Your code here:
    pass

# Test the functions if this module is run directly
if __name__ == "__main__":
    print("Testing unit conversions:")
    
    # Test temperature conversions
    print("\nTemperature conversions:")
    print(f"0°C = {celsius_to_fahrenheit(0)}°F")
    print(f"100°C = {celsius_to_fahrenheit(100)}°F")
    print(f"32°F = {fahrenheit_to_celsius(32)}°C")
    print(f"212°F = {fahrenheit_to_celsius(212)}°C")
    print(f"0°C = {celsius_to_kelvin(0)}K")
    print(f"273.15K = {kelvin_to_celsius(273.15)}°C")
    
    # Test length conversions
    print("\nLength conversions:")
    print(f"1 inch = {inches_to_cm(1)} cm")
    print(f"1 cm = {cm_to_inches(1)} inches")
    print(f"1 foot = {feet_to_meters(1)} meters")
    print(f"1 meter = {meters_to_feet(1)} feet")
    print(f"1 mile = {miles_to_km(1)} km")
    print(f"1 km = {km_to_miles(1)} miles")
    
    # Test weight/mass conversions
    print("\nWeight/Mass conversions:")
    print(f"1 pound = {pounds_to_kg(1)} kg")
    print(f"1 kg = {kg_to_pounds(1)} pounds")
    print(f"1 ounce = {ounces_to_grams(1)} grams")
    print(f"1 gram = {grams_to_ounces(1)} ounces")
    
    # Test volume conversions
    print("\nVolume conversions:")
    print(f"1 gallon = {gallons_to_liters(1)} liters")
    print(f"1 liter = {liters_to_gallons(1)} gallons")
    
    # Test time conversions
    print("\nTime conversions:")
    print(f"1 hour = {hours_to_minutes(1)} minutes")
    print(f"1 minute = {minutes_to_seconds(1)} seconds")
    print(f"1 day = {days_to_hours(1)} hours")
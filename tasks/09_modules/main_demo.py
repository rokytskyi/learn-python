# main_demo.py
# This file demonstrates the __name__ == "__main__" pattern

def main_function():
    """
    This is the main function of the program.
    It contains the main logic of the program.
    """
    print("This is the main function.")
    print("It contains the main logic of the program.")
    return "Main function executed successfully"

# This code only runs when the script is executed directly
if __name__ == "__main__":
    print("This script is being run directly.")
    result = main_function()
    print(f"Result: {result}")
else:
    print("This script has been imported as a module.")
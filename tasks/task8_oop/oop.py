# Task 8: Object-Oriented Programming
# Complete the exercises below

# 1. Create a simple class with attributes and methods
# Your code here:
# Example:
# class Dog:
#     """A simple class representing a dog."""
#     
#     # Class attribute (shared by all instances)
#     species = "Canis familiaris"
#     
#     # Instance attributes and methods
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     
#     def description(self):
#         return f"{self.name} is {self.age} years old"
#     
#     def speak(self, sound):
#         return f"{self.name} says {sound}"
# 
# # Create instances of the Dog class
# dog1 = Dog("Buddy", 5)
# dog2 = Dog("Max", 3)
# 
# # Access attributes and call methods
# print(f"{dog1.name} is a {dog1.species}")
# print(dog1.description())
# print(dog1.speak("Woof!"))
# print(dog2.description())
# print(dog2.speak("Bark!"))


# 2. Implement encapsulation with private attributes and getter/setter methods
# Your code here:
# Example:
# class BankAccount:
#     """A class representing a bank account with private attributes."""
#     
#     def __init__(self, account_number, balance):
#         self.__account_number = account_number  # Private attribute
#         self.__balance = balance  # Private attribute
#     
#     # Getter methods
#     def get_account_number(self):
#         return self.__account_number
#     
#     def get_balance(self):
#         return self.__balance
#     
#     # Setter method
#     def set_balance(self, balance):
#         if balance >= 0:
#             self.__balance = balance
#         else:
#             print("Balance cannot be negative")
#     
#     # Other methods
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             return f"Deposited ${amount}. New balance: ${self.__balance}"
#         else:
#             return "Deposit amount must be positive"
#     
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             return f"Withdrew ${amount}. New balance: ${self.__balance}"
#         else:
#             return "Invalid withdrawal amount"
# 
# # Create a bank account
# account = BankAccount("12345", 1000)
# 
# # Access attributes using getter methods
# print(f"Account Number: {account.get_account_number()}")
# print(f"Balance: ${account.get_balance()}")
# 
# # Use methods to modify the balance
# print(account.deposit(500))
# print(account.withdraw(200))
# 
# # Try to access private attribute directly (will show a different name due to name mangling)
# try:
#     print(account.__balance)  # This will raise an AttributeError
# except AttributeError as e:
#     print(f"Error: {e}")


# 3. Create class hierarchies using inheritance
# Your code here:
# Example:
# class Animal:
#     """Base class for animals."""
#     
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#     
#     def make_sound(self):
#         return "Some generic animal sound"
#     
#     def __str__(self):
#         return f"{self.name} is a {self.species}"
# 
# 
# class Cat(Animal):
#     """A cat class that inherits from Animal."""
#     
#     def __init__(self, name, breed):
#         # Call the parent class's __init__ method
#         super().__init__(name, species="Cat")
#         self.breed = breed
#     
#     def make_sound(self):
#         # Override the parent's method
#         return "Meow!"
# 
# 
# class Dog(Animal):
#     """A dog class that inherits from Animal."""
#     
#     def __init__(self, name, breed):
#         # Call the parent class's __init__ method
#         super().__init__(name, species="Dog")
#         self.breed = breed
#     
#     def make_sound(self):
#         # Override the parent's method
#         return "Woof!"
#     
#     def fetch(self, item):
#         # Add a method specific to dogs
#         return f"{self.name} fetches the {item}"
# 
# 
# # Create instances of the classes
# animal = Animal("Generic Animal", "Unknown")
# cat = Cat("Whiskers", "Siamese")
# dog = Dog("Rex", "German Shepherd")
# 
# # Use the objects
# print(animal)
# print(f"{animal.name} says: {animal.make_sound()}")
# 
# print(cat)
# print(f"{cat.name} is a {cat.breed} {cat.species}")
# print(f"{cat.name} says: {cat.make_sound()}")
# 
# print(dog)
# print(f"{dog.name} is a {dog.breed} {dog.species}")
# print(f"{dog.name} says: {dog.make_sound()}")
# print(dog.fetch("ball"))


# 4. Implement method overriding and polymorphism
# Your code here:
# Example:
# class Shape:
#     """Base class for shapes."""
#     
#     def area(self):
#         """Calculate the area of the shape."""
#         raise NotImplementedError("Subclasses must implement this method")
#     
#     def perimeter(self):
#         """Calculate the perimeter of the shape."""
#         raise NotImplementedError("Subclasses must implement this method")
#     
#     def description(self):
#         """Return a description of the shape."""
#         return "This is a generic shape"
# 
# 
# class Rectangle(Shape):
#     """A rectangle shape."""
#     
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     
#     def area(self):
#         return self.width * self.height
#     
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#     
#     def description(self):
#         return f"Rectangle with width {self.width} and height {self.height}"
# 
# 
# class Circle(Shape):
#     """A circle shape."""
#     
#     def __init__(self, radius):
#         self.radius = radius
#     
#     def area(self):
#         import math
#         return math.pi * self.radius ** 2
#     
#     def perimeter(self):
#         import math
#         return 2 * math.pi * self.radius
#     
#     def description(self):
#         return f"Circle with radius {self.radius}"
# 
# 
# # Create instances of different shapes
# shapes = [Rectangle(5, 10), Circle(7)]
# 
# # Demonstrate polymorphism by calling the same methods on different objects
# for shape in shapes:
#     print(shape.description())
#     print(f"Area: {shape.area():.2f}")
#     print(f"Perimeter: {shape.perimeter():.2f}")
#     print()


# 5. Use special methods (magic methods) for operator overloading
# Your code here:
# Example:
# class Vector:
#     """A 2D vector class with operator overloading."""
#     
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     
#     def __str__(self):
#         """String representation for print()."""
#         return f"Vector({self.x}, {self.y})"
#     
#     def __repr__(self):
#         """String representation for debugging."""
#         return f"Vector({self.x}, {self.y})"
#     
#     def __add__(self, other):
#         """Vector addition with + operator."""
#         return Vector(self.x + other.x, self.y + other.y)
#     
#     def __sub__(self, other):
#         """Vector subtraction with - operator."""
#         return Vector(self.x - other.x, self.y - other.y)
#     
#     def __mul__(self, scalar):
#         """Vector multiplication with * operator."""
#         return Vector(self.x * scalar, self.y * scalar)
#     
#     def __eq__(self, other):
#         """Vector equality with == operator."""
#         return self.x == other.x and self.y == other.y
#     
#     def __abs__(self):
#         """Vector magnitude with abs() function."""
#         return (self.x ** 2 + self.y ** 2) ** 0.5
# 
# 
# # Create vectors
# v1 = Vector(3, 4)
# v2 = Vector(1, 2)
# 
# # Use operator overloading
# print(f"v1 = {v1}")
# print(f"v2 = {v2}")
# print(f"v1 + v2 = {v1 + v2}")
# print(f"v1 - v2 = {v1 - v2}")
# print(f"v1 * 2 = {v1 * 2}")
# print(f"abs(v1) = {abs(v1)}")
# print(f"v1 == v2: {v1 == v2}")
# print(f"v1 == Vector(3, 4): {v1 == Vector(3, 4)}")


# 6. Create and use class methods and static methods
# Your code here:
# Example:
# class MathUtils:
#     """A utility class with class and static methods."""
#     
#     # Class variable
#     pi = 3.14159
#     
#     @classmethod
#     def circle_area(cls, radius):
#         """Calculate the area of a circle using the class's pi value."""
#         return cls.pi * radius ** 2
#     
#     @classmethod
#     def update_pi(cls, new_pi):
#         """Update the pi value."""
#         cls.pi = new_pi
#     
#     @staticmethod
#     def add(a, b):
#         """Add two numbers."""
#         return a + b
#     
#     @staticmethod
#     def subtract(a, b):
#         """Subtract b from a."""
#         return a - b
# 
# 
# # Use class methods
# print(f"Default pi: {MathUtils.pi}")
# print(f"Circle area with radius 5: {MathUtils.circle_area(5)}")
# 
# # Update the class variable
# MathUtils.update_pi(3.14)
# print(f"Updated pi: {MathUtils.pi}")
# print(f"Circle area with radius 5 (updated pi): {MathUtils.circle_area(5)}")
# 
# # Use static methods
# print(f"5 + 3 = {MathUtils.add(5, 3)}")
# print(f"10 - 4 = {MathUtils.subtract(10, 4)}")
# 
# # Create an instance (not typically needed for utility classes)
# math = MathUtils()
# print(f"Using instance: 7 + 2 = {math.add(7, 2)}")  # Still works


# Real-World Task: Library Management System
# This task will help you apply object-oriented programming concepts in a practical context.

# Import necessary modules
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# Abstract base class for library items
class LibraryItem(ABC):
    """Abstract base class for all library items."""
    
    def __init__(self, title, item_id, publication_year):
        """Initialize a library item with basic attributes."""
        self.__title = title
        self.__item_id = item_id
        self.__publication_year = publication_year
        self.__checked_out = False
        self.__checked_out_to = None
        self.__due_date = None
    
    # Getter methods
    def get_title(self):
        """Get the title of the item."""
        return self.__title
    
    def get_item_id(self):
        """Get the ID of the item."""
        return self.__item_id
    
    def get_publication_year(self):
        """Get the publication year of the item."""
        return self.__publication_year
    
    def is_checked_out(self):
        """Check if the item is currently checked out."""
        return self.__checked_out
    
    def get_checked_out_to(self):
        """Get the patron who has checked out the item."""
        return self.__checked_out_to
    
    def get_due_date(self):
        """Get the due date for the item."""
        return self.__due_date
    
    # Setter methods
    def set_checked_out(self, status, patron=None, due_date=None):
        """Set the checked out status of the item."""
        self.__checked_out = status
        self.__checked_out_to = patron if status else None
        self.__due_date = due_date if status else None
    
    # Abstract methods that subclasses must implement
    @abstractmethod
    def get_checkout_period(self):
        """Return the standard checkout period for this type of item in days."""
        pass
    
    @abstractmethod
    def get_daily_fine(self):
        """Return the daily fine for overdue items of this type."""
        pass
    
    # Special methods
    def __str__(self):
        """Return a string representation of the item."""
        status = f"Checked Out to {self.__checked_out_to} until {self.__due_date}" if self.__checked_out else "Available"
        return f"{self.__title} ({self.__publication_year}) - {status}"
    
    def __eq__(self, other):
        """Check if two library items are the same based on their ID."""
        if not isinstance(other, LibraryItem):
            return False
        return self.__item_id == other.get_item_id()


# Concrete subclasses of LibraryItem
class Book(LibraryItem):
    """Class representing a book in the library."""
    
    def __init__(self, title, item_id, publication_year, author, isbn, genre):
        """Initialize a book with its attributes."""
        super().__init__(title, item_id, publication_year)
        self.__author = author
        self.__isbn = isbn
        self.__genre = genre
    
    # Getter methods
    def get_author(self):
        """Get the author of the book."""
        return self.__author
    
    def get_isbn(self):
        """Get the ISBN of the book."""
        return self.__isbn
    
    def get_genre(self):
        """Get the genre of the book."""
        return self.__genre
    
    # Implementation of abstract methods
    def get_checkout_period(self):
        """Books can be checked out for 21 days."""
        return 21
    
    def get_daily_fine(self):
        """Fine for overdue books is $0.25 per day."""
        return 0.25
    
    # Special methods
    def __str__(self):
        """Return a string representation of the book."""
        base_str = super().__str__()
        return f"Book: {base_str}, Author: {self.__author}, ISBN: {self.__isbn}, Genre: {self.__genre}"


class Magazine(LibraryItem):
    """Class representing a magazine in the library."""
    
    def __init__(self, title, item_id, publication_year, issue_number, publisher):
        """Initialize a magazine with its attributes."""
        super().__init__(title, item_id, publication_year)
        self.__issue_number = issue_number
        self.__publisher = publisher
    
    # Getter methods
    def get_issue_number(self):
        """Get the issue number of the magazine."""
        return self.__issue_number
    
    def get_publisher(self):
        """Get the publisher of the magazine."""
        return self.__publisher
    
    # Implementation of abstract methods
    def get_checkout_period(self):
        """Magazines can be checked out for 7 days."""
        return 7
    
    def get_daily_fine(self):
        """Fine for overdue magazines is $0.50 per day."""
        return 0.50
    
    # Special methods
    def __str__(self):
        """Return a string representation of the magazine."""
        base_str = super().__str__()
        return f"Magazine: {base_str}, Issue: {self.__issue_number}, Publisher: {self.__publisher}"


class DVD(LibraryItem):
    """Class representing a DVD in the library."""
    
    def __init__(self, title, item_id, publication_year, director, runtime):
        """Initialize a DVD with its attributes."""
        super().__init__(title, item_id, publication_year)
        self.__director = director
        self.__runtime = runtime  # in minutes
    
    # Getter methods
    def get_director(self):
        """Get the director of the DVD."""
        return self.__director
    
    def get_runtime(self):
        """Get the runtime of the DVD in minutes."""
        return self.__runtime
    
    # Implementation of abstract methods
    def get_checkout_period(self):
        """DVDs can be checked out for 14 days."""
        return 14
    
    def get_daily_fine(self):
        """Fine for overdue DVDs is $1.00 per day."""
        return 1.00
    
    # Special methods
    def __str__(self):
        """Return a string representation of the DVD."""
        base_str = super().__str__()
        return f"DVD: {base_str}, Director: {self.__director}, Runtime: {self.__runtime} minutes"


# Patron class
class Patron:
    """Class representing a library patron."""
    
    def __init__(self, patron_id, name, email, phone=None):
        """Initialize a patron with their information."""
        self.__patron_id = patron_id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__checked_out_items = []  # List of items currently checked out
    
    # Getter methods
    def get_patron_id(self):
        """Get the patron's ID."""
        return self.__patron_id
    
    def get_name(self):
        """Get the patron's name."""
        return self.__name
    
    def get_email(self):
        """Get the patron's email."""
        return self.__email
    
    def get_phone(self):
        """Get the patron's phone number."""
        return self.__phone
    
    def get_checked_out_items(self):
        """Get the list of items checked out by the patron."""
        return self.__checked_out_items.copy()  # Return a copy to prevent direct modification
    
    # Setter methods
    def set_email(self, email):
        """Update the patron's email."""
        self.__email = email
    
    def set_phone(self, phone):
        """Update the patron's phone number."""
        self.__phone = phone
    
    # Methods for checking out and returning items
    def add_checked_out_item(self, item):
        """Add an item to the patron's checked out items."""
        if item not in self.__checked_out_items:
            self.__checked_out_items.append(item)
    
    def remove_checked_out_item(self, item):
        """Remove an item from the patron's checked out items."""
        if item in self.__checked_out_items:
            self.__checked_out_items.remove(item)
    
    # Special methods
    def __str__(self):
        """Return a string representation of the patron."""
        return f"{self.__name} (ID: {self.__patron_id})"
    
    def __eq__(self, other):
        """Check if two patrons are the same based on their ID."""
        if not isinstance(other, Patron):
            return False
        return self.__patron_id == other.get_patron_id()


# Library class
class Library:
    """Class representing a library that manages items and patrons."""
    
    # Class variable to track the next available IDs
    next_item_id = 1
    next_patron_id = 1
    
    def __init__(self, name):
        """Initialize a library with a name."""
        self.__name = name
        self.__items = {}  # Dictionary of items by ID
        self.__patrons = {}  # Dictionary of patrons by ID
    
    # Class methods for generating IDs
    @classmethod
    def generate_item_id(cls):
        """Generate a unique item ID."""
        item_id = f"I{cls.next_item_id:04d}"
        cls.next_item_id += 1
        return item_id
    
    @classmethod
    def generate_patron_id(cls):
        """Generate a unique patron ID."""
        patron_id = f"P{cls.next_patron_id:04d}"
        cls.next_patron_id += 1
        return patron_id
    
    # Methods for managing items
    def add_item(self, item):
        """Add an item to the library."""
        # Your code here:
        # 1. Check if the item is a LibraryItem
        # 2. Add the item to the items dictionary
        # 3. Return success message
        pass
    
    def remove_item(self, item_id):
        """Remove an item from the library."""
        # Your code here:
        # 1. Check if the item exists
        # 2. Check if the item is checked out
        # 3. Remove the item from the items dictionary
        # 4. Return success message
        pass
    
    def get_item(self, item_id):
        """Get an item by its ID."""
        # Your code here:
        # 1. Check if the item exists
        # 2. Return the item or None
        pass
    
    def search_items(self, search_term, search_type="title"):
        """Search for items by title, author, or genre."""
        # Your code here:
        # 1. Implement search logic based on search_type
        # 2. Return a list of matching items
        pass
    
    # Methods for managing patrons
    def add_patron(self, name, email, phone=None):
        """Add a new patron to the library."""
        # Your code here:
        # 1. Generate a new patron ID
        # 2. Create a new Patron object
        # 3. Add the patron to the patrons dictionary
        # 4. Return the new patron
        pass
    
    def remove_patron(self, patron_id):
        """Remove a patron from the library."""
        # Your code here:
        # 1. Check if the patron exists
        # 2. Check if the patron has checked out items
        # 3. Remove the patron from the patrons dictionary
        # 4. Return success message
        pass
    
    def get_patron(self, patron_id):
        """Get a patron by their ID."""
        # Your code here:
        # 1. Check if the patron exists
        # 2. Return the patron or None
        pass
    
    # Methods for checkout operations
    def check_out_item(self, item_id, patron_id, due_date=None):
        """Check out an item to a patron."""
        # Your code here:
        # 1. Get the item and patron
        # 2. Check if the item is available
        # 3. Calculate the due date if not provided
        # 4. Update the item's status
        # 5. Add the item to the patron's checked out items
        # 6. Return success message
        pass
    
    def return_item(self, item_id):
        """Return an item to the library."""
        # Your code here:
        # 1. Get the item
        # 2. Check if the item is checked out
        # 3. Get the patron who has the item
        # 4. Update the item's status
        # 5. Remove the item from the patron's checked out items
        # 6. Calculate any fines if the item is overdue
        # 7. Return success message and fine amount
        pass
    
    def calculate_fine(self, item, return_date=None):
        """Calculate the fine for an overdue item."""
        # Your code here:
        # 1. Check if the item is checked out
        # 2. Get the due date
        # 3. Calculate the number of days overdue
        # 4. Calculate the fine based on the item's daily fine rate
        # 5. Return the fine amount
        pass
    
    # Methods for generating reports
    def get_all_items(self):
        """Get a list of all items in the library."""
        return list(self.__items.values())
    
    def get_all_patrons(self):
        """Get a list of all patrons registered with the library."""
        return list(self.__patrons.values())
    
    def get_checked_out_items(self):
        """Get a list of all items that are currently checked out."""
        # Your code here:
        # 1. Filter the items to find those that are checked out
        # 2. Return the list of checked out items
        pass
    
    def get_overdue_items(self):
        """Get a list of all items that are currently overdue."""
        # Your code here:
        # 1. Get the current date
        # 2. Filter the checked out items to find those that are overdue
        # 3. Return the list of overdue items
        pass
    
    # Special methods
    def __str__(self):
        """Return a string representation of the library."""
        return f"{self.__name} Library with {len(self.__items)} items and {len(self.__patrons)} patrons"


# Command-line interface functions
def display_menu():
    """Display the main menu options."""
    print("\nLIBRARY MANAGEMENT SYSTEM")
    print("=========================")
    print("\nMain Menu:")
    print("1. Add a book")
    print("2. Add a patron")
    print("3. Check out a book")
    print("4. Return a book")
    print("5. Search for books")
    print("6. View all books")
    print("7. View all patrons")
    print("8. View checked out books")
    print("9. Exit")

def add_book_ui(library):
    """UI for adding a book to the library."""
    # Your code here:
    # 1. Get book details from user input
    # 2. Create a Book object
    # 3. Add the book to the library
    # 4. Display success message
    pass

def add_patron_ui(library):
    """UI for adding a patron to the library."""
    # Your code here:
    # 1. Get patron details from user input
    # 2. Add the patron to the library
    # 3. Display success message
    pass

def check_out_book_ui(library):
    """UI for checking out a book to a patron."""
    # Your code here:
    # 1. Get patron ID from user
    # 2. Get book ID from user
    # 3. Get due date from user (optional)
    # 4. Check out the book
    # 5. Display success message
    pass

def return_book_ui(library):
    """UI for returning a book to the library."""
    # Your code here:
    # 1. Get book ID from user
    # 2. Return the book
    # 3. Display success message and any fines
    pass

def search_books_ui(library):
    """UI for searching for books."""
    # Your code here:
    # 1. Get search term from user
    # 2. Get search type from user (title, author, genre)
    # 3. Search for books
    # 4. Display search results
    pass

def view_all_books_ui(library):
    """UI for viewing all books in the library."""
    # Your code here:
    # 1. Get all books from the library
    # 2. Display the books in a formatted way
    pass

def view_all_patrons_ui(library):
    """UI for viewing all patrons registered with the library."""
    # Your code here:
    # 1. Get all patrons from the library
    # 2. Display the patrons in a formatted way
    pass

def view_checked_out_books_ui(library):
    """UI for viewing all books that are currently checked out."""
    # Your code here:
    # 1. Get all checked out books from the library
    # 2. Display the books in a formatted way
    pass

def main():
    """Main function to run the library management system."""
    # Create a library
    library = Library("Community")
    
    # Add some sample data
    # Add books
    book1 = Book("The Great Gatsby", Library.generate_item_id(), 1925, "F. Scott Fitzgerald", "9780743273565", "Fiction")
    book2 = Book("To Kill a Mockingbird", Library.generate_item_id(), 1960, "Harper Lee", "9780061120084", "Fiction")
    book3 = Book("1984", Library.generate_item_id(), 1949, "George Orwell", "9780451524935", "Science Fiction")
    
    library.add_item(book1)
    library.add_item(book2)
    library.add_item(book3)
    
    # Add patrons
    patron1 = library.add_patron("John Smith", "john@example.com", "555-123-4567")
    patron2 = library.add_patron("Jane Doe", "jane@example.com", "555-987-6543")
    
    # Main loop
    while True:
        display_menu()
        
        try:
            choice = int(input("\nEnter your choice: "))
            
            if choice == 1:
                add_book_ui(library)
            elif choice == 2:
                add_patron_ui(library)
            elif choice == 3:
                check_out_book_ui(library)
            elif choice == 4:
                return_book_ui(library)
            elif choice == 5:
                search_books_ui(library)
            elif choice == 6:
                view_all_books_ui(library)
            elif choice == 7:
                view_all_patrons_ui(library)
            elif choice == 8:
                view_checked_out_books_ui(library)
            elif choice == 9:
                print("\nThank you for using the Library Management System. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 9.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")
        except Exception as e:
            print(f"\nAn error occurred: {e}")

# Uncomment the line below to run the library management system
# if __name__ == "__main__":
#     main()
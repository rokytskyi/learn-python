# Task 8: Object-Oriented Programming

## Objective
Learn the principles of object-oriented programming (OOP) in Python, including classes, objects, inheritance, and polymorphism.

## Instructions
1. Create a simple class with attributes and methods
2. Implement object instantiation and method calls
3. Use constructors and destructors
4. Implement encapsulation with private attributes and getter/setter methods
5. Create class hierarchies using inheritance
6. Implement method overriding and polymorphism
7. Use special methods (magic methods) for operator overloading
8. Create and use class methods and static methods

## Concepts to Learn
- Classes and objects
- Attributes and methods
- Constructors (`__init__`) and destructors (`__del__`)
- Instance methods
- Encapsulation and access modifiers
- Inheritance and method overriding
- Multiple inheritance
- Polymorphism
- Special methods (`__str__`, `__repr__`, `__eq__`, etc.)
- Class methods and static methods
- Abstract base classes

## Expected Output
```
Basic class usage:
[Output showing class instantiation and method calls]

Encapsulation:
[Output demonstrating private attributes and getter/setter methods]

Inheritance:
[Output showing inheritance and method overriding]

Polymorphism:
[Output demonstrating polymorphic behavior]

Special methods:
[Output showing operator overloading with special methods]

Class and static methods:
[Output demonstrating class and static methods]
```

## Real-World Task: Library Management System

Create a library management system that allows librarians to manage books, patrons, and borrowing operations. This task will help you apply object-oriented programming concepts in a practical context that can be verified.

### Requirements:
1. Create the following classes:
   - `Book`: Represents a book in the library
   - `Patron`: Represents a library patron (user)
   - `Library`: Manages the collection of books and patrons
   - At least one abstract base class (e.g., `LibraryItem`)
   - At least one inheritance hierarchy (e.g., different types of library items)

2. Implement the following features:
   - Add and remove books from the library
   - Register and remove patrons
   - Check out books to patrons
   - Return books to the library
   - Search for books by title, author, or genre
   - Track overdue books and calculate fines
   - Generate reports (e.g., books checked out, available books)

3. Use OOP concepts:
   - Encapsulation: Use private attributes with getter/setter methods
   - Inheritance: Create a hierarchy of library items (books, magazines, DVDs)
   - Polymorphism: Implement methods that behave differently for different item types
   - Special methods: Implement `__str__`, `__repr__`, `__eq__`, etc.
   - Class methods: Implement methods that operate on the class level
   - Static methods: Implement utility methods that don't require instance or class state

4. Implement a simple command-line interface to interact with the system

### Verification Criteria:
Your library management system should:
- Successfully create and manage Book and Patron objects
- Allow books to be added to and removed from the library
- Allow patrons to be registered and removed
- Support checking out and returning books
- Track which books are checked out to which patrons
- Calculate due dates and fines for overdue books
- Implement proper encapsulation of attributes
- Use inheritance to create different types of library items
- Use polymorphism for operations that differ by item type
- Implement appropriate special methods
- Include at least one class method and one static method
- Have a functional command-line interface

### Example Output:
```
LIBRARY MANAGEMENT SYSTEM
=========================

Main Menu:
1. Add a book
2. Add a patron
3. Check out a book
4. Return a book
5. Search for books
6. View all books
7. View all patrons
8. View checked out books
9. Exit

Enter your choice: 1

Add a Book:
Title: The Great Gatsby
Author: F. Scott Fitzgerald
ISBN: 9780743273565
Genre: Fiction
Publication Year: 1925

Book added successfully!

Main Menu:
...

Enter your choice: 3

Check Out a Book:
Enter patron ID: P001
Enter book ISBN: 9780743273565
Enter due date (YYYY-MM-DD): 2025-09-15

Book checked out successfully!

Main Menu:
...

Enter your choice: 6

All Books:
---------
1. Title: The Great Gatsby
   Author: F. Scott Fitzgerald
   ISBN: 9780743273565
   Genre: Fiction
   Status: Checked Out to John Smith (P001)
   Due Date: 2025-09-15

2. Title: To Kill a Mockingbird
   Author: Harper Lee
   ISBN: 9780061120084
   Genre: Fiction
   Status: Available

3. Title: 1984
   Author: George Orwell
   ISBN: 9780451524935
   Genre: Science Fiction
   Status: Available
```

## Tips
- Class names in Python typically use CamelCase
- The `self` parameter refers to the instance and must be the first parameter of instance methods
- Use double underscores (`__`) prefix for private attributes
- The `super()` function can be used to call methods from a parent class
- Method overriding allows a subclass to provide a specific implementation of a method defined in its parent class
- Special methods (magic methods) allow classes to emulate built-in types or implement operator overloading
- Class methods receive the class as their first argument and are defined with the `@classmethod` decorator
- Static methods don't operate on the instance or class and are defined with the `@staticmethod` decorator
- Abstract base classes define a common interface for subclasses and can be created using the `abc` module
- Consider using composition in addition to inheritance where appropriate
- Use type hints to make your code more readable and maintainable
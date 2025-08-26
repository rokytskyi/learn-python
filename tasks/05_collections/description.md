# Task 5: Lists and Dictionaries

## Objective
Learn how to work with Python's collection data types, focusing on lists and dictionaries, to store and manipulate multiple values.

## Instructions
1. Create and manipulate lists using various operations
2. Use list methods (append, insert, remove, etc.)
3. Implement list comprehensions for concise list creation
4. Create and manipulate dictionaries
5. Access and modify dictionary values
6. Iterate through lists and dictionaries
7. Implement nested data structures (lists within lists, dictionaries within dictionaries)

## Concepts to Learn
- List creation and indexing
- List slicing
- List methods (append, extend, insert, remove, pop, sort, reverse)
- List comprehensions
- Dictionary creation and access
- Dictionary methods (keys, values, items, get, update)
- Iterating through collections with loops
- Nested data structures
- Common collection patterns

## Expected Output
```
List operations:
[Output showing list creation and manipulation]

List methods:
[Output demonstrating various list methods]

List comprehensions:
[Output showing list comprehensions]

Dictionary operations:
[Output showing dictionary creation and access]

Dictionary methods:
[Output demonstrating various dictionary methods]

Iteration examples:
[Output showing iteration through collections]

Nested structures:
[Output demonstrating nested data structures]
```

## Real-World Task: Contact Management System

Create a contact management system that allows users to store, retrieve, and manage contact information. This task will help you apply list and dictionary concepts in a practical context that can be verified.

### Requirements:
1. Create a system that can:
   - Add new contacts with details (name, phone, email, address, etc.)
   - View all contacts
   - Search for contacts by name
   - Update contact information
   - Delete contacts
   - Group contacts by categories (e.g., family, friends, work)
   - Sort contacts by different criteria (e.g., name, category)

2. Use appropriate data structures:
   - Store contacts in a list of dictionaries
   - Use dictionaries for each contact's details
   - Use nested structures for organizing contacts by groups
   - Use list comprehensions for filtering and searching

3. Implement a simple command-line interface to interact with the system

### Verification Criteria:
Your contact management system should:
- Successfully store and retrieve contact information
- Allow adding, viewing, updating, and deleting contacts
- Support searching for contacts by name (partial matches should work)
- Enable grouping contacts into categories
- Support sorting contacts by different fields
- Handle edge cases (e.g., duplicate contacts, empty fields)
- Use appropriate list and dictionary operations for each function
- Use list comprehensions where appropriate
- Have a functional command-line interface

### Example Output:
```
CONTACT MANAGEMENT SYSTEM
=========================

Main Menu:
1. Add a new contact
2. View all contacts
3. Search for a contact
4. Update a contact
5. Delete a contact
6. View contacts by category
7. Sort contacts
8. Exit

Enter your choice: 1

Add a new contact:
Name: John Smith
Phone: 555-123-4567
Email: john@example.com
Address: 123 Main St
Category (family/friend/work/other): work

Contact added successfully!

Main Menu:
...

Enter your choice: 2

All Contacts:
-------------
1. John Smith (work)
   Phone: 555-123-4567
   Email: john@example.com
   Address: 123 Main St

2. Jane Doe (family)
   Phone: 555-987-6543
   Email: jane@example.com
   Address: 456 Oak Ave

Main Menu:
...

Enter your choice: 3

Search for a contact:
Enter name to search: John

Search Results:
--------------
1. John Smith (work)
   Phone: 555-123-4567
   Email: john@example.com
   Address: 123 Main St
```

## Tips
- Lists are ordered, mutable collections that can contain mixed data types
- List indices start at 0
- Negative indices count from the end of the list
- List slicing syntax is `list[start:end:step]`
- List comprehensions provide a concise way to create lists
- Dictionaries store key-value pairs and provide fast lookups
- Dictionary keys must be immutable (strings, numbers, tuples)
- Use the `in` operator to check if a key exists in a dictionary
- The `.get()` method provides a safe way to access dictionary values with a default
- Nested structures are powerful but can become complex - keep them organized
- Consider using functions to organize your code for different operations
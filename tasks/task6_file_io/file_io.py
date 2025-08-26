# Task 6: File I/O
# Complete the exercises below

# 1. Create a text file and write content to it
# Your code here:
# Example:
# # Method 1: Open, write, close
# file = open("sample.txt", "w")
# file.write("Hello, world!\n")
# file.write("This is a sample text file.\n")
# file.close()
# 
# print("File created successfully.")


# 2. Read content from a text file
# Your code here:
# Example:
# # Method 1: Read entire file
# file = open("sample.txt", "r")
# content = file.read()
# file.close()
# 
# print("File content (read):")
# print(content)
# 
# # Method 2: Read line by line
# file = open("sample.txt", "r")
# lines = file.readlines()
# file.close()
# 
# print("File content (readlines):")
# for i, line in enumerate(lines, 1):
#     print(f"Line {i}: {line.strip()}")


# 3. Append content to an existing file
# Your code here:
# Example:
# file = open("sample.txt", "a")
# file.write("This line was appended.\n")
# file.write("Another appended line.\n")
# file.close()
# 
# print("Content appended to file.")
# 
# # Read the updated file
# file = open("sample.txt", "r")
# updated_content = file.read()
# file.close()
# 
# print("Updated file content:")
# print(updated_content)


# 4. Work with file paths using the os module
# Your code here:
# Example:
# import os
# 
# # Get current working directory
# current_dir = os.getcwd()
# print(f"Current directory: {current_dir}")
# 
# # Join paths in a platform-independent way
# file_path = os.path.join(current_dir, "data", "sample.txt")
# print(f"Full file path: {file_path}")
# 
# # Check if a file exists
# if os.path.exists("sample.txt"):
#     print("sample.txt exists")
# else:
#     print("sample.txt does not exist")
# 
# # Get file information
# if os.path.exists("sample.txt"):
#     size = os.path.getsize("sample.txt")
#     print(f"File size: {size} bytes")


# 5. Use context managers (with statement) for file operations
# Your code here:
# Example:
# # Writing with context manager
# with open("context_sample.txt", "w") as file:
#     file.write("Using context manager for file operations.\n")
#     file.write("No need to explicitly close the file.\n")
# 
# print("File written using context manager.")
# 
# # Reading with context manager
# with open("context_sample.txt", "r") as file:
#     content = file.read()
# 
# print("Content from context manager file:")
# print(content)


# 6. Read and write CSV files
# Your code here:
# Example:
# import csv
# 
# # Writing CSV
# data = [
#     ["Name", "Age", "City"],
#     ["Alice", 30, "New York"],
#     ["Bob", 25, "Los Angeles"],
#     ["Charlie", 35, "Chicago"]
# ]
# 
# with open("people.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
# 
# print("CSV file written successfully.")
# 
# # Reading CSV
# with open("people.csv", "r") as file:
#     reader = csv.reader(file)
#     print("CSV file content:")
#     for row in reader:
#         print(row)
# 
# # Using DictReader and DictWriter
# dict_data = [
#     {"Name": "David", "Age": 28, "City": "Boston"},
#     {"Name": "Eve", "Age": 22, "City": "Miami"},
#     {"Name": "Frank", "Age": 45, "City": "Seattle"}
# ]
# 
# with open("people_dict.csv", "w", newline="") as file:
#     fieldnames = ["Name", "Age", "City"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(dict_data)
# 
# print("Dict CSV file written successfully.")


# 7. Work with JSON files
# Your code here:
# Example:
# import json
# 
# # Create data structure
# person = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York",
#     "languages": ["Python", "JavaScript", "Java"],
#     "is_student": False,
#     "contact": {
#         "email": "alice@example.com",
#         "phone": "123-456-7890"
#     }
# }
# 
# # Write JSON to file
# with open("person.json", "w") as file:
#     json.dump(person, file, indent=4)
# 
# print("JSON file written successfully.")
# 
# # Read JSON from file
# with open("person.json", "r") as file:
#     loaded_person = json.load(file)
# 
# print("JSON file content:")
# print(json.dumps(loaded_person, indent=2))
# 
# # Access specific data
# print(f"Name: {loaded_person['name']}")
# print(f"Languages: {', '.join(loaded_person['languages'])}")
# print(f"Email: {loaded_person['contact']['email']}")


# Real-World Task: Note-Taking Application
# This task will help you apply file I/O concepts in a practical context.

# Import necessary modules
import os
import json
import datetime
import shutil  # For file operations like copying

# Constants
NOTES_DIR = "notes"  # Directory to store notes
INDEX_FILE = os.path.join(NOTES_DIR, "index.json")  # Master index file

# Ensure the notes directory exists
def setup_notes_directory():
    """Create the notes directory if it doesn't exist."""
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)
        print(f"Created notes directory: {NOTES_DIR}")
    
    # Create an empty index file if it doesn't exist
    if not os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, "w") as f:
            json.dump([], f)
        print("Created empty index file")

# Function to get a list of all notes from the index
def get_notes_index():
    """Read the master index file and return the list of notes."""
    try:
        with open(INDEX_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or is invalid, return an empty list
        return []

# Function to save the notes index
def save_notes_index(notes_index):
    """Save the notes index to the master index file."""
    with open(INDEX_FILE, "w") as f:
        json.dump(notes_index, f, indent=4)

# Function to create a new note
def create_note():
    """Create a new note with title, content, and tags."""
    # Your code here:
    # 1. Get note title, tags, and content from user
    # 2. Create a unique filename based on the title
    # 3. Save the note content to a text file
    # 4. Create metadata (title, date, tags) and save as JSON
    # 5. Update the master index
    pass

# Function to view a note
def view_note():
    """Display the content and metadata of a selected note."""
    # Your code here:
    # 1. List all available notes
    # 2. Ask user to select a note
    # 3. Read the note file and metadata
    # 4. Display the note content and metadata
    pass

# Function to edit a note
def edit_note():
    """Edit the content or metadata of an existing note."""
    # Your code here:
    # 1. List all available notes
    # 2. Ask user to select a note
    # 3. Read the current note content and metadata
    # 4. Ask what to edit (content, title, or tags)
    # 5. Update the note file and metadata
    # 6. Update the master index if necessary
    pass

# Function to delete a note
def delete_note():
    """Delete a note and remove it from the index."""
    # Your code here:
    # 1. List all available notes
    # 2. Ask user to select a note
    # 3. Confirm deletion
    # 4. Remove the note file and metadata
    # 5. Update the master index
    pass

# Function to list all notes
def list_notes():
    """Display a list of all available notes with their metadata."""
    # Your code here:
    # 1. Read the master index
    # 2. Display each note with its title, creation date, and tags
    # 3. Handle the case when no notes exist
    pass

# Function to search notes
def search_notes():
    """Search for notes by title or content."""
    # Your code here:
    # 1. Ask for search term
    # 2. Search through note titles and content
    # 3. Display matching notes
    # 4. Handle case when no matches are found
    pass

# Function to export a note
def export_note():
    """Export a note to plain text or JSON format."""
    # Your code here:
    # 1. List all available notes
    # 2. Ask user to select a note
    # 3. Ask for export format (text or JSON)
    # 4. Ask for export location
    # 5. Export the note to the specified format and location
    pass

# Display the main menu
def display_menu():
    """Display the main menu options."""
    print("\nNOTE-TAKING APPLICATION")
    print("=======================")
    print("\nMain Menu:")
    print("1. Create a new note")
    print("2. View a note")
    print("3. Edit a note")
    print("4. Delete a note")
    print("5. List all notes")
    print("6. Search notes")
    print("7. Export a note")
    print("8. Exit")

# Main function to run the note-taking application
def main():
    """Run the note-taking application."""
    # Ensure the notes directory exists
    setup_notes_directory()
    
    while True:
        display_menu()
        
        try:
            choice = int(input("\nEnter your choice: "))
            
            if choice == 1:
                create_note()
            elif choice == 2:
                view_note()
            elif choice == 3:
                edit_note()
            elif choice == 4:
                delete_note()
            elif choice == 5:
                list_notes()
            elif choice == 6:
                search_notes()
            elif choice == 7:
                export_note()
            elif choice == 8:
                print("\nThank you for using the Note-Taking Application. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 8.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")
        except Exception as e:
            print(f"\nAn error occurred: {e}")

# Uncomment the line below to run the note-taking application
# if __name__ == "__main__":
#     main()
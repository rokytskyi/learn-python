# Task 6: File I/O

## Objective
Learn how to read from and write to files in Python, including different file formats and methods for file handling.

## Instructions
1. Create a text file and write content to it
2. Read content from a text file
3. Append content to an existing file
4. Work with file paths using the `os` module
5. Use context managers (`with` statement) for file operations
6. Read and write CSV files
7. Work with JSON files

## Concepts to Learn
- File opening modes (`'r'`, `'w'`, `'a'`, `'b'`)
- Reading file content (read(), readline(), readlines())
- Writing to files (write(), writelines())
- File paths and the `os` module
- Context managers for file handling
- Working with CSV files using the `csv` module
- Working with JSON files using the `json` module
- Error handling for file operations

## Expected Output
```
Text file operations:
[Output showing text file creation and reading]

File appending:
[Output showing appending to a file]

File path operations:
[Output showing file path manipulation]

Context manager usage:
[Output showing file operations with context managers]

CSV file operations:
[Output showing CSV reading and writing]

JSON file operations:
[Output showing JSON reading and writing]
```

## Real-World Task: Note-Taking Application

Create a simple note-taking application that allows users to create, view, edit, and organize notes. This task will help you apply file I/O concepts in a practical context that can be verified.

### Requirements:
1. Create a note-taking application with the following features:
   - Create new notes with a title and content
   - View existing notes
   - Edit existing notes
   - Delete notes
   - List all available notes
   - Search for notes by title or content
   - Categorize notes with tags
   - Export notes to different formats (plain text and JSON)

2. File operations to implement:
   - Save each note as a separate text file
   - Use JSON to store metadata (title, creation date, tags, etc.)
   - Use a master index file to keep track of all notes
   - Implement proper file path handling for cross-platform compatibility
   - Use context managers for all file operations
   - Handle file operation errors gracefully

3. Implement a simple command-line interface to interact with the application

### Verification Criteria:
Your note-taking application should:
- Successfully create, read, update, and delete note files
- Store and retrieve note metadata correctly
- Maintain a master index of all notes
- Handle file paths correctly across different operating systems
- Use context managers for all file operations
- Handle errors gracefully (file not found, permission issues, etc.)
- Support searching through notes
- Support categorizing notes with tags
- Allow exporting notes to different formats
- Have a functional command-line interface

### Example Output:
```
NOTE-TAKING APPLICATION
=======================

Main Menu:
1. Create a new note
2. View a note
3. Edit a note
4. Delete a note
5. List all notes
6. Search notes
7. Export a note
8. Exit

Enter your choice: 1

Create a new note:
Title: Meeting Notes
Tags (comma-separated): work, project, planning
Enter note content (type 'END' on a new line when finished):
Meeting with the team on August 26, 2025.
Action items:
- Complete project proposal
- Schedule follow-up meeting
- Distribute minutes to team
END

Note saved successfully!

Main Menu:
...

Enter your choice: 5

All Notes:
----------
1. Meeting Notes (Tags: work, project, planning) - Created: 2025-08-26
2. Shopping List (Tags: personal) - Created: 2025-08-25
3. Project Ideas (Tags: work, ideas) - Created: 2025-08-24

Main Menu:
...

Enter your choice: 2

View a note:
Enter note number: 1

Title: Meeting Notes
Created: August 26, 2025
Tags: work, project, planning

Content:
Meeting with the team on August 26, 2025.
Action items:
- Complete project proposal
- Schedule follow-up meeting
- Distribute minutes to team
```

## Tips
- Always close files after opening them, or use context managers (`with` statement)
- Use appropriate file modes: 'r' for reading, 'w' for writing (overwrites), 'a' for appending
- Add 'b' to the mode for binary files (e.g., 'rb', 'wb')
- The `os.path` module helps with platform-independent file path operations
- CSV files can be read/written using the `csv` module
- JSON files can be read/written using the `json` module
- Use try/except blocks to handle file operation errors
- Check if a file exists before trying to read it using `os.path.exists()`
- Remember that writing to a file with mode 'w' will overwrite any existing content
- Consider creating a dedicated directory for storing notes
- Use meaningful filenames based on note titles or IDs
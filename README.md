# File-management CLI

A command-line file manager written in Python. It lets you create, read, update, and delete text files in the current folder from a simple menu.

## Features

- **Create** a new text file and write content to it
- **Read** the contents of an existing file
- **Update** a file by renaming it, overwriting its content, or appending to it
- **Delete** a file
- Lists the files available before each operation so you can pick one

## Requirements

- Python 3.8 or higher
- No external libraries. The project uses only the standard library (`pathlib`).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

## Usage

Run the program:

```bash
python file_manager.py
```

You will see a menu:

```
press 1 for creating a new file
press 2 for reading an existing file
press 3 for updating an existing file
press 4 for deleting an existing file
```

Enter the number of the action you want and follow the prompts.

## Project Structure

```
.
├── file_manager.py   # Main program with all CRUD operations
|___ main.py
└── README.md
```

## How It Works

Each operation is a separate function:

| Function        | Purpose                                      |
|-----------------|----------------------------------------------|
| `fileinfolder()`| Lists files in the working directory         |
| `creat_file()`  | Creates a file and writes user input to it   |
| `read_file()`   | Displays the contents of a file              |
| `update_file()` | Renames, overwrites, or appends to a file    |
| `delete_file()` | Deletes a file                               |
| `input_1()`     | Reads the menu choice and calls the function |

## Known Limitations

- Overwriting or deleting a file has no undo.
- Only text files are supported.

## Future Improvements

- [ ] Refactor the code into a `FileManager` class
- [ ] Add a command-line interface with `argparse`
- [ ] Add unit tests with `pytest`
- [ ] Log each operation to a file

## What I Learned
From this I learned many of new methods and function to do CRUD operation on files of the system and understood how important is it to manage our system files and folder. 
 

## Author

Hardik singh
KIET Group of Institutions CSE

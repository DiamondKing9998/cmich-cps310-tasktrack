# TaskTrack

A command-line task manager created for CPS 310.

## Current Features

- View tasks
- Add tasks
- Save tasks to tasks.txt file
- Auto-load tasks from tasks.txt file

## Requirements

-Python 3

## Project Files

-`tasktrack.py` - The actual program's Python file
-`tasks.txt` - Example tasks file that contains the tasks the program reads/writes to
-`.gitignore` - Tells Git what files to ignore sending to the repo

## Running the Program

 - Run command-line via VS Code: Menu Button -> Terminal -> New:
 ```text
 python tasktrack.py
 ```
 ## Task Persistence

When the program starts, it reads the task list from `tasks.txt` by calling `load_tasks()`.
Each non-empty line in the file is treated as one task, so the file acts like a simple list of tasks with one task per line.

If `tasks.txt` does not exist yet, the program prints a message and starts with an empty task list.
The project includes a `save_tasks()` function that writes tasks back to the file, but in the current version it is not called automatically after adding a task. That means tasks are currently loaded at startup and kept in memory during the session, rather than being saved back to disk immediately.

## Sample Interaction

```text
$ python tasktrack.py

TaskTrack Menu
1. View tasks
2. Add task
3. Exit
Choose an option: 1

Tasks:
1. Complete ICA04
2. Review GitHub commands
3. Update the TaskTrack README
4. Test persistent storage

TaskTrack Menu
1. View tasks
2. Add task
3. Exit
Choose an option: 2
Enter a new task: Submit assignment
Task added successfully.

TaskTrack Menu
1. View tasks
2. Add task
3. Exit
Choose an option: 3
Goodbye!
```

## Current Limitation

Tasks cannot be removed/completed from tasks.txt using the program.

## Version Control

This project is managed with Git for local version control. As changes are made to files such as `tasktrack.py`, `tasks.txt`, and `README.md`, they can be saved in a Git repository with commits that track the history of the project.

GitHub can also be used as the remote repository for this project, allowing the code to be pushed online for backup, sharing, and collaboration. A typical workflow is to initialize or connect the local repository, add files with `git add`, commit changes with `git commit -m "message"`, and push them to GitHub with `git push`.

This setup makes it easy to review progress over time, restore earlier versions, and collaborate with others on the TaskTrack program.
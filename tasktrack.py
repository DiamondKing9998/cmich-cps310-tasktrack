"""A command-line task manager created for CPS 310.

Author: Carson Warren
Course: CPS 310
"""

TASKS_FILE = "tasks.txt"

def load_tasks(filename):
    """Load tasks from a text file and return them as a list."""
    tasks = []

    try:
        with open(filename, "r") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
    except FileNotFoundError:
        print("No file found.")
        return []

    return tasks


def display_menu():
    """Display the available TaskTrack menu options."""
    print("\nTaskTrack Menu")
    print("1. View tasks")
    print("2. Add task")
    print("3. Exit")


def add_task(tasks):
    """Add a task to the list, prompting the user if no task is provided."""
    task = input("Enter a new task: ").strip()
    if not task:
        print("A task cannot be empty.")
        return
    tasks.append(task)
    print("Task added successfully.")


def view_tasks(tasks):
    """Display all tasks currently stored in the task list."""
    if not tasks:
        print("No tasks available.")
        return

    print("\nTasks:")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def save_tasks(tasks, filename):
    """Save tasks to a text file."""
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")


def main():
    """Run the TaskTrack menu until the user chooses to exit."""
    tasks = load_tasks(TASKS_FILE)

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
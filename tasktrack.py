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
    print("3. Remove task")
    print("4. Exit")


def add_task(tasks):
    """Add a task to the list, prompting the user if no task is provided."""
    task = input("Enter a new task: ").strip()
    if not task:
        print("A task cannot be empty.")
        return
    tasks.append(task)
    save_tasks(tasks, TASKS_FILE)
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

def remove_task(tasks):
    """Prompt the user to select and remove a task.

    Return True when a task is removed and False otherwise.
    """
    if not tasks:
        print("No tasks are available to remove.")
        return False

    view_tasks(tasks)

    while True:
        selection = input("Enter the number of the task to remove: ").strip()

        if not selection.isdigit():
            print("Please enter a valid task number.")
            break

        task_number = int(selection)
        
        if task_number < 1 or task_number > len(tasks):
            print("That task number does not exist.")
            return False
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks, TASKS_FILE)
            print(f"Task '{removed_task}' removed successfully.")
            break
        else:
            print("Please enter a valid task number.")

    return True


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
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
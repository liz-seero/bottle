import json
import os

# Constants
DATA_FILE = 'todo_list.json'

# Utility Functions

def load_data():
    """Load tasks from the JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

def save_data(tasks):
    """Save tasks to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def print_tasks(tasks):
    """Print all tasks with their details."""
    if not tasks:
        print("No tasks available.")
        return
    print("\nTo-Do List:")
    for i, task in enumerate(tasks):
        status = "Completed" if task['completed'] else "Pending"
        print(f"{i + 1}. {task['title']} - {status}")
    print()

# Task Management Functions

def add_task(tasks):
    """Add a new task to the list."""
    title = input("Enter the task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return
    tasks.append({'title': title, 'completed': False})
    save_data(tasks)
    print("Task added successfully.")

def delete_task(tasks):
    """Delete a task from the list."""
    print_tasks(tasks)
    try:
        task_index = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
            save_data(tasks)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def mark_task_completed(tasks):
    """Mark a task as completed."""
    print_tasks(tasks)
    try:
        task_index = int(input("Enter the number of the task to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]['completed'] = True
            save_data(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def view_tasks(tasks):
    """View all tasks."""
    print_tasks(tasks)

# Main Function

def main():
    """Main function to run the to-do list application."""
    tasks = load_data()

    while True:
        print("To-Do List Application")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task Completed")
        print("4. View Tasks")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            delete_task(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            view_tasks(tasks)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()

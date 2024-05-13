class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def remove_task(self, index):
        if index < 1 or index > len(self.tasks):
            print("Invalid task index.")
        else:
            removed_task = self.tasks.pop(index - 1)
            print(f"Task '{removed_task}' removed.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            index = int(input("Enter index of task to remove: "))
            todo_list.remove_task(index)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

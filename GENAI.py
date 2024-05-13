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


class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)
        print("Expense added successfully.")

    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total expenses: ${total:.2f}")

    def expenses_by_category(self):
        categories = {}
        for expense in self.expenses:
            if expense.category in categories:
                categories[expense.category] += expense.amount
            else:
                categories[expense.category] = expense.amount

        print("Expenses by category:")
        for category, amount in categories.items():
            print(f"{category}: ${amount:.2f}")


def main():
    expense_tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. View Expenses by Category")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: $"))
            expense = Expense(category, amount)
            expense_tracker.add_expense(expense)
        elif choice == "2":
            expense_tracker.total_expenses()
        elif choice == "3":
            expense_tracker.expenses_by_category()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


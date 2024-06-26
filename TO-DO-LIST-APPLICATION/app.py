class ToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Added task: '{task}'")

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f"Marked task {task_index + 1} as completed")
        else:
            print("Invalid task index")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i + 1}. {task['task']} [{status}]")

def main():
    todo = ToDo()

    while True:
        print("\nTo-Do List Application")
        print("1. Add a task")
        print("2. Mark a task as completed")
        print("3. View current tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo.add_task(task)
        elif choice == "2":
            try:
                task_index = int(input("Enter the task number to mark as completed: ")) - 1
                todo.mark_completed(task_index)
            except ValueError:
                print("Invalid input, please enter a valid task number.")
        elif choice == "3":
            todo.view_tasks()
        elif choice == "4":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please select a valid option.")

if __name__ == "__main__":
    main()

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def delete_task(self, index):
        del self.tasks[index]

    def complete_task(self, index):
        self.tasks[index]["completed"] = True

    def display_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{i + 1}. {task['task']} - {status}")

def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added.")

        elif choice == "2":
            if todo_list.tasks:
                index = int(input("Enter the index of the task to delete: ")) - 1
                if 0 <= index < len(todo_list.tasks):
                    todo_list.delete_task(index)
                    print("Task deleted.")
                else:
                    print("Invalid index.")
            else:
                print("No tasks to delete.")

        elif choice == "3":
            if todo_list.tasks:
                index = int(input("Enter the index of the task to mark as completed: ")) - 1
                if 0 <= index < len(todo_list.tasks):
                    todo_list.complete_task(index)
                    print("Task marked as completed.")
                else:
                    print("Invalid index.")
            else:
                print("No tasks to mark as completed.")

        elif choice == "4":
            print("\nTasks:")
            todo_list.display_tasks()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()

from todo import Task


def load_tasks():
    tasks = []
    try:
        with open("todos.txt", "r") as f:
            for line in f:
                completed, description = line.strip().split("|")
                tasks.append(Task(description, completed == "True"))
    except FileNotFoundError:
        pass
    return tasks


def save_tasks(tasks):
    with open("todos.txt", "w") as f:
        for task in tasks:
            f.write(f"{task.completed}|{task.description}\n")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            desc = input("Enter task description: ")
            tasks.append(Task(desc))
            save_tasks(tasks)
            print("Task added!")
        elif choice == "3":
            view_tasks(tasks)
            num = int(input("Enter task number to mark done: "))
            if 1 <= num <= len(tasks):
                tasks[num-1].mark_done()
                save_tasks(tasks)
                print("Task marked as done!")
            else:
                print("Invalid task number.")
        elif choice == "4":
            view_tasks(tasks)
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num-1)
                save_tasks(tasks)
                print("Task deleted!")
            else:
                print("Invalid task number.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

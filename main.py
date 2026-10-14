"""Command-line task tracker for Git practice."""

from task_manager import add_task, list_tasks, complete_task


def show_menu():
    print("\nSimple Task Tracker")
    print("1. List tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Exit")


def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            title = input("Task title: ").strip()
            if title:
                add_task(tasks, title)
                print("Task added.")
            else:
                print("Task title cannot be empty.")
        elif choice == "3":
            list_tasks(tasks)
            try:
                task_number = int(input("Task number to complete: "))
                complete_task(tasks, task_number - 1)
            except ValueError:
                print("Enter a valid task number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()

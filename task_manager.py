"""Functions for managing tasks."""

# Making tweaks to practice .py file


def add_task(tasks, title):
    tasks.append({"title": title, "completed": False})


def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not done"
        print(f"{index}. {task['title']} [{status}]")


def complete_task(tasks, index):
    if index < 0 or index >= len(tasks):
        print("That task number does not exist.")
        return

    tasks[index]["completed"] = True
    print("Task marked as complete.")

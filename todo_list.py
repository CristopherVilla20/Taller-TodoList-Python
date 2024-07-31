def add_task(tasks):
    """Add a new task to the to-do list."""
    task = input("Enter a new task: ")
    due_date = input("Due date (YYYY-MM-DD): ")
    importance = input("Importance (1-4): ")
    tasks.append([task, due_date, importance])
    print(f"Task '{task}' added.")

def list_tasks(tasks):
    """List all the tasks in the to-do list."""
    if not tasks:
        print("No tasks available.")
    else:
        for index, task_info in enumerate(tasks, start=1):
            task, due_date, importance = task_info
            print(f"{index}. {task} (Due: {due_date}, Importance: {importance})")

def edit_task(tasks):
    """Edit an existing task."""
    if not tasks:
        print("No tasks available.")
        return

    task_index = int(input("Enter the number of the task you want to edit: ")) - 1
    if 0 <= task_index < len(tasks):
        task_info = tasks[task_index]
        new_task = input("Enter the new task: ")
        new_due_date = input("Enter the new due date (YYYY-MM-DD): ")
        new_importance = input("Enter the new importance (1-4): ")
        tasks[task_index] = [new_task, new_due_date, new_importance]
        print("Task edited successfully.")
    else:
        print("Invalid task number.")

def clear_list(tasks):
    """Clear the entire to-do list."""
    tasks.clear()
    print("To-do list cleared.")

def main():
    tasks = []
    while True:
        print("\nTo-do List Manager")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Edit an existing task")
        print("4. Clear the entire list")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            clear_list(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

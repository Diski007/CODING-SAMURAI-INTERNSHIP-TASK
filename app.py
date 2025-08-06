FILENAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Initialize task list from file
tasks = load_tasks()

# Main loop
while True:
    try:
        operation = int(input("Enter:\n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit/Stop\nYour choice: "))
        
        if operation == 1:
            add = input("Enter task you want to add: ")
            tasks.append(add)
            save_tasks(tasks)
            print(f"Task '{add}' has been successfully added.\n")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update: ")
            if updated_val in tasks:
                up = input("Enter new task: ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                save_tasks(tasks)
                print(f"Updated task to '{up}'\n")
            else:
                print("Task not found.\n")

        elif operation == 3:
            del_val = input("Which task do you want to delete: ")
            if del_val in tasks:
                tasks.remove(del_val)
                save_tasks(tasks)
                print(f"Task '{del_val}' deleted.\n")
            else:
                print("Task not found.\n")

        elif operation == 4:
            if not tasks:
                print("No tasks to show.\n")
            else:
                print("Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                print()

        elif operation == 5:
            print("Exiting program.")
            break

        else:
            print("Invalid input. Please choose a number between 1 and 5.\n")

    except ValueError:
        print("Invalid input. Please enter a number.\n")

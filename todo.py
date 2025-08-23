tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter choice: ")

    
    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")

    
    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    
    elif choice == "3":
        if not tasks:
            print("No tasks to update.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            task_num = int(input("Enter task number to update: "))
            if 0 < task_num <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[task_num - 1] = new_task
                print("Task updated!")
            else:
                print("Invalid task number.")

    
    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            task_num = int(input("Enter task number to delete: "))
            if 0 < task_num <= len(tasks):
                tasks.pop(task_num - 1)
                print("Task deleted!")
            else:
                print("Invalid task number.")

    
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")

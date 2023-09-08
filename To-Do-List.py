tasks = []

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Display tasks")
    print("3. Remove a task")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")
        
    elif choice == '2':
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("To-Do List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == '3':
        if not tasks:
            print("Your to-do list is empty.")
        else:
            try:
                task_number = int(input("Enter the task number to remove: "))
                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Task '{removed_task}' removed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
                
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")





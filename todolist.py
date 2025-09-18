def todo_list():
    tasks = []
    
    while True:
        print("\n=== To-Do List ===")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            task = input("Enter task: ")
            tasks.append({"task": task, "done": False})
            print("Task added successfully!")
            
        elif choice == '2':
            if not tasks:
                print("No tasks in your list!")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    status = "✓" if task["done"] else " "
                    print(f"{i}. [{status}] {task['task']}")
                    
        elif choice == '3':
            if not tasks:
                print("No tasks to mark as done!")
            else:
                try:
                    task_num = int(input("Enter task number to mark as done: ")) - 1
                    if 0 <= task_num < len(tasks):
                        tasks[task_num]["done"] = True
                        print("Task marked as done!")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Please enter a valid number!")
                    
        elif choice == '4':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Please try again.")

todo_list()
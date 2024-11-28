def task_manager():
    tasks = []  # Empty list to store tasks

    print("----WELCOME TO THE TASK MANAGEMENT APP----")

    total_task = int(input("Enter how many tasks you want to add: "))  # Get the number of tasks to add

    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")  # Get each task name
        tasks.append(task_name)

    print(f"Today's tasks are:\n{tasks}")

    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n"))

        if operation == 1:
            add = input("Enter task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added.")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update: ")

            if updated_val in tasks:
                up = input("Enter new task: ")
                ind = tasks.index(updated_val)  # Find the index of the task to update
                tasks[ind] = up
                print(f"Updated task to '{up}'")
            else:
                print("Task not found.")

        elif operation == 3:
            del_task = input("Enter the task name you want to delete: ")

            if del_task in tasks:
                tasks.remove(del_task)  # Remove the task from the list
                print(f"Task '{del_task}' has been deleted.")
            else:
                print("Task not found.")

        elif operation == 4:
            print(f"Current tasks are:\n{tasks}")

        elif operation == 5:
            print("Exiting the task manager. Have a great day!")
            break

        else:
            print("Invalid option. Please enter a number between 1 and 5.")

# Run the task manager
task_manager()


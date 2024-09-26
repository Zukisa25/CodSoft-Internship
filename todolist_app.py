# To-do List Application
# Create, update, and track user to-do lists
# 15 May 2024

print("\n======== To-do List App ========\n")

task_title          = []
task_description    = []
task_status         = []

while True:
       
        print("(1) Add Task")
        print("(2) Complete Task")
        print("(3) Delete Task")
        print("(4) View Tasks")
        print("(5) Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            
            title = input("Enter task title: ")
            task_title.append(title)
            description = input("Enter task description: ")
            task_description.append(description)
            task_status.append("Pending")

            print("Task added successfully.\n")
        
        elif choice == "2":      
            task_index = int(input("Enter index of task to mark as completed: ")) - 1
            
            if 0 <= task_index < len(task_status):
                task_status [task_index] = "Completed"
                print("Task", task_index +1, "completed.\n" )

            else:
                print("Invalid task index.\n")

        
        elif choice == "3":
            task_index = int(input("Enter index of task to be deleted: ")) - 1
            
            if 0 <= task_index < len(task_status):
                task_title.pop(task_index)
                task_description.pop(task_index)
                task_status.pop(task_index)

                print("Task deleted successfully.\n")
                
            else:
                print("Invalid task index.\n")
        
        elif choice == "4": 
            if len(task_status) <= 0:
                print("Task list is empty.\n")
            
            else:
                for num_task in range(1, len(task_status) +1):
                    print(f"{num_task}. {task_title[num_task-1]} - {task_description[num_task-1]} [{task_status[num_task-1]}]")
                print()


        elif choice == "5":
            print("Exiting...\n")
            break
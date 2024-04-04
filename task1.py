def welcome_message():
  print("Welcome to the To-Do List App!")

def display_menu():
  print("\nMenu:")
  print("1. Add a task")
  print("2. View tasks")
  print("3. Mark a task as complete")
  print("4. Delete a task")
  print("5. Quit")

def get_user_choice():
  while True:
    try:
      choice = int(input("Enter your choice: "))
      if 1 <= choice <= 5:
        return choice
      else:
        print("Invalid choice. Please enter a number between 1 and 5.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def create_task():
  task_title = input("Enter task title: ")
  tasks.append({"title": task_title, "status": "Incomplete"})
  print(f"Task '{task_title}' added successfully!")

def view_tasks():
  if not tasks:
    print("There are no tasks in the list.")
  else:
    print("\nTasks:")
    for index, task in enumerate(tasks):
      print(f"{index+1}. {task['title']} ({task['status']})")

def mark_task_complete():
  view_tasks()
  if not tasks:
    return

  while True:
    try:
      task_number = int(input("Enter the number of the task to mark complete: "))
      if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["status"] = "Complete"
        print(f"Task '{tasks[task_number - 1]['title']}' marked as complete!")
        return
      else:
        print("Invalid task number. Please enter a number between 1 and", len(tasks))
    except ValueError:
      print("Invalid input. Please enter a number.")

def delete_task():
  """Allows user to delete a task."""
  view_tasks()
  if not tasks:
    return

  while True:
    try:
      task_number = int(input("Enter the number of the task to delete: "))
      if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        print(f"Task deleted successfully!")
        return
      else:
        print("Invalid task number. Please enter a number between 1 and", len(tasks))
    except ValueError:
      print("Invalid input. Please enter a number.")

tasks = []  
while True:
  welcome_message()
  display_menu()
  choice = get_user_choice()

  if choice == 1:
    create_task()
  elif choice == 2:
    view_tasks()
  elif choice == 3:
    mark_task_complete()
  elif choice == 4:
    delete_task()
  elif choice == 5:
    print("Exiting the To-Do List App.")
    break
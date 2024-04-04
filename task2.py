STATUS_OPTIONS = ("Incomplete", "Complete")

def display_menu():
  print("\nWelcome to the To-Do List App!")
  print("\nMenu:")
  print("1. sweep")
  print("2. View tasks")
  print("3. Mark a task as complete")
  print("4. Delete a task")
  print("5. Quit")


def get_task_title():
  while True:
    title = input("\n Sweep (or leave blank for 'Incomplete'): ")
    if title.strip():  
      return title
    else:
      print("sweep.")


def display_tasks(tasks):

  if not tasks:
    print("\nNo tasks in the list.")
  else:
    print("\nYour Tasks:")
    for index, task in enumerate(tasks):
      print(f"{index+1}. {task['title']} ({task['status']})")


def add_task(tasks):
  title = get_task_title()
  tasks.append({"title": title, "status": STATUS_OPTIONS[0]})  
  print(f"\nTask '{title}' added to the list.")


def mark_task_complete(tasks):
  display_tasks(tasks)
  if not tasks:
    return

  while True:
    try:
      task_number = int(input("\nEnter the number of the task to mark complete: "))
      if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["status"] = STATUS_OPTIONS[1]
        print(f"\nTask '{tasks[task_number - 1]['title']}' marked complete.")
        return
      else:
        print("Invalid task number. Please enter a number between 1 and", len(tasks))
    except ValueError:
      print("Invalid input. Please enter a number.")


def delete_task(tasks):
  display_tasks(tasks)
  if not tasks:
    return

  while True:
    try:
      task_number = int(input("\nEnter the number of the task to delete: "))
      if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        print(f"\nTask '{task_number}' deleted from the list.")
        return
      else:
        print("Invalid task number. Please enter a number between 1 and", len(tasks))
    except ValueError:
      print("Invalid input. Please enter a number.")


def main():
  
  tasks = []  

  while True:
    display_menu()
    try:
      choice = int(input("Enter your choice (1-5): "))
      if choice == 1:
        add_task(tasks)
      elif choice == 2:
        display_tasks(tasks)
      elif choice == 3:
        mark_task_complete(tasks)
      elif choice == 4:
        delete_task(tasks)
      elif choice == 5:
        print("\nExiting To-Do List App.")
        break
      else:
        print("Invalid choice. Please enter a number between 1 and 5.")
    except ValueError:
      print("Invalid input. Please enter a number.")

if __name__ == "__main__":
  main()
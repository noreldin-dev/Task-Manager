import json
import os

# Global list to store tasks
tasks = []
# The filename where data will be saved
DATA_FILE = "tasks_data.json"

def load_tasks():
    """Loads tasks from a JSON file when the program starts."""
    global tasks
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                tasks = json.load(file)
        except (json.JSONDecodeError, IOError):
            print("⚠️ Warning: Could not read save file. Starting with an empty list.")
            tasks = []
    else:
        tasks = []

def save_tasks():
    """Saves the current task list to a JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
    except IOError:
        print("❌ Error: Could not save data to file.")

def add_tasks():
    """Adds a new task to the list and saves changes."""
    task_name = input("Enter task description: ").strip()
    if task_name:
        task_info = {"task": task_name, "completed": False}
        tasks.append(task_info)
        save_tasks()
        print("✅ Task added successfully.")
    else:
        print("❌ Task cannot be empty.")

def mark_task_complete():
    """Marks a selected incomplete task as finished and saves changes."""
    incomplete_tasks = [task for task in tasks if not task["completed"]]
    
    if not incomplete_tasks:
        print("ℹ️ No pending tasks to complete.")
        return

    print("\n--- Pending Tasks ---")
    for i, task in enumerate(incomplete_tasks):
        print(f"{i+1}. {task['task']}")
    
    try:
        choice = int(input("Enter task number to mark as complete: "))
        if 1 <= choice <= len(incomplete_tasks):
            # Update the task status in the global list
            incomplete_tasks[choice - 1]["completed"] = True
            save_tasks()
            print("✅ Task marked as completed.")
        else:
            print("❌ Invalid selection.")
    except ValueError:
        print("❌ Error: Please enter a valid number.")

def view_tasks():
    """Displays all tasks with their current status."""
    if not tasks:
        print("ℹ️ Your task list is empty.")
        return

    print("\n" + "="*30)
    print("      YOUR TASK LIST")
    print("="*30)
    for i, task in enumerate(tasks):
        status = "✔" if task["completed"] else "❌"
        print(f"{i+1}. [{status}] {task['task']}")
    print("="*30)

def main():
    """Main application loop."""
    load_tasks()  # Load existing data at startup
    
    menu = """
1 - Add Task
2 - Mark Task as Complete
3 - View All Tasks
4 - Quit
"""
    
    print("Welcome to your Task Management System")
    while True:
        print(menu)
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            add_tasks()
        elif choice == "2":
            mark_task_complete()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Saving data and exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
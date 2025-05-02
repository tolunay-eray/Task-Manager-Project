import os
import json

def initialize_json_file():
    if not os.path.exists("tasks.json"): # Checks if the file exists
        with open("tasks.json","w") as f:
            json.dump([],f)

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f) # converted json to python data type
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json","w") as f:
        json.dump(tasks,f,indent=4)

def add_task():
    description = input("Task Description:")
    task = {"description":description,"completed":False}
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added")

def list_tasks():
    tasks=load_tasks()
    if not tasks:
        print("No tasks yet")
    else:
        for i ,task in enumerate(tasks):
            status = "✅" if task["completed"] else "❌"
            print(f"{i + 1}. {task['description']} [{status}]")

def mark_task_done():
    list_tasks() # First we list the tasks
    try:
        index = int(input("Completed task number: ")) - 1 # index starts from 0 in python
        tasks = load_tasks()
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("✔️ Task marked as completed.")
    except (ValueError, IndexError):
        print("❌ Invalid selection.")

def delete_task():
    list_tasks()
    try:
        index = int(input("Silinecek görev numarası: ")) - 1
        tasks = load_tasks()
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"🗑️ '{removed['description']}' deleted.")
    except (ValueError, IndexError):
        print("❌ Invalid selection.")

def main():
    initialize_json_file()
    while True:
        print("\n=== TASK MANAGER ===")
        print("1. List Tasks")
        print("2. Add New Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Your choice (1-5): ")

        if choice == "1":
            list_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 See You Later!")
            break
        else:
            print("❌ Invalid Choice.")

if __name__ == "__main__":
    main()








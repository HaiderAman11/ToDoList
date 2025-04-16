def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_menu():
    print("\n📝 To-Do List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

tasks = load_tasks()

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    elif choice == "2":
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        save_tasks(tasks)
        print("✅ Task added!")
    elif choice == "3":
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"❌ Task '{removed}' deleted!")
        else:
            print("Invalid task number!")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please choose a valid option.")


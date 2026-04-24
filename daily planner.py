import json

# Load existing tasks
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except:
    tasks = []

while True:
    print("\nDaily Planner")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})

        # Save tasks
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)

        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks, start=1):
                status = "Done" if t["done"] else "Not Done"
                print(f"{i}. {t['task']} - {status}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to update.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t['task']}")

            num = int(input("Enter task number: "))
            tasks[num - 1]["done"] = True

            # Save updated tasks
            with open("tasks.json", "w") as file:
                json.dump(tasks, file)

            print("Task marked as done!")

    elif choice == "4":
        break

    else:
        print("Invalid choice")
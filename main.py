import sys, json, os
from datetime import datetime

args = sys.argv[1:]

filename = "tasks.json"
tasks = []

if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        tasks = json.load(f)

def updatedTask(id, new_task):
    for task in tasks:
        if task["id"] == id:
            task["name"] = new_task
            task["updatedAt"] = str(datetime.now())
            return True
    return False

def deletedTask(id):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return True
    return False

def markedInProgress(id):
    for task in tasks:
        if task["id"] == id:
            task["status"] = "in-progress"
            return True
    return False

def markedDone(id):
    for task in tasks:
        if task["id"] == id:
            task["status"] = "done"
            return True
    return False

if len(args) == 2 and args[0] == "add":
    task_id = 1 if len(tasks) == 0 else tasks[-1]["id"] + 1
    tasks.append({"name": args[1], "id": task_id, "status": "todo", "createdAt": str(datetime.now()), "updatedAt": str(datetime.now())})
    print(f"Task added successfully (ID: {task_id})")
elif len(args) == 3 and args[0] == "update":
    if args[1].isdigit() and updatedTask(int(args[1]), args[2]):
        print(f"Task {int(args[1])} updated")
    else:
        print("Invalid input. Correct format: update task_id new_task")
elif len(args) == 2 and args[0] == "delete":
    if args[1].isdigit() and deletedTask(int(args[1])):
        print(f"Task {int(args[1])} deleted")
    else:
        print("Invalid input. Correct format: delete task_id")
elif len(args) == 2 and args[0] == "mark-in-progress":
    if args[1].isdigit() and markedInProgress(int(args[1])):
        print(f"Task {int(args[1])} marked in progress")
    else:
        print("Invalid input. Correct format: mark-in-progress task_id")
elif len(args) == 2 and args[0] == "mark-done":
    if args[1].isdigit() and markedDone(int(args[1])):
        print(f"Task {int(args[1])} marked done")
    else:
        print("Invalid input. Correct format: mark-done task_id")
elif len(args) == 1 and args[0] == "list":
    print(f"{"id":<5}{"task":<20}{"status":<15}")
    # id占5字符左对齐，task占20字符左对齐，status占15字符左对齐
    for task in tasks:
        print(f"{task["id"]:<5}{task["name"]:<20}{task["status"]:<15}")
    # 中文占2格宽度，而:<按字符算，所以task为中文时status对不齐
elif len(args) == 2 and args[0] == "list":
    if args[1] == "todo":
        print(f"{"id":<5}{"task":<20}{"status":<15}")
        for task in tasks:
            if task["status"] == "todo":
                print(f"{task["id"]:<5}{task["name"]:<20}{task["status"]:<15}")
    elif args[1] == "in-progress":
        print(f"{"id":<5}{"task":<20}{"status":<15}")
        for task in tasks:
            if task["status"] == "in-progress":
                print(f"{task["id"]:<5}{task["name"]:<20}{task["status"]:<15}")
    elif args[1] == "done":
        print(f"{"id":<5}{"task":<20}{"status":<15}")
        for task in tasks:
            if task["status"] == "done":
                print(f"{task["id"]:<5}{task["name"]:<20}{task["status"]:<15}")
    elif args[1] == "not-done":
        print(f"{"id":<5}{"task":<20}{"status":<15}")
        for task in tasks:
            if task["status"] != "done":
                print(f"{task["id"]:<5}{task["name"]:<20}{task["status"]:<15}")
    else:
        print("Invalid input. Correct format: list [todo/in-progress/done/not-done]")
else:
    print("Invalid input.")

with open(filename, "w", encoding="utf-8") as f:
    json.dump(tasks, f, ensure_ascii=False, indent=4) # 能写入中文；缩进4格
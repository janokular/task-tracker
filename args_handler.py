import json
import time

def handle(args, task_json):
    # Add new task to tasks.json
    if args.action == 'add':
        with open(task_json, 'r+') as tasks:
            # Load data from tasks.json
            tasks_data = json.load(tasks)

            # Check if there are any tasks inside the tasks.json
            # If not set it to 1 else increment the value for new_task_id
            if not tasks_data["tasks"]:
                new_task_id = 1
            else:
                new_task_id = tasks_data["tasks"][-1].get("id") + 1

            # Create new task to be saved
            new_task = {
                'id': new_task_id,
                'description': args.task,
                'status': 'todo',
                'createdAt': time.asctime(),
                'updatedAt': time.asctime()
            }

            # Append the task to the loaded data
            tasks_data["tasks"].append(new_task)
            tasks.seek(0)

            # Save the task inside the tasks.json
            json.dump(tasks_data, tasks, indent=4)

    elif args.action == 'update':
        print(args.task_id)
        print(args.task)

    elif args.action == 'delete':
        print(args.task_id)

    elif args.action == 'mark-in-progress':
        print(args.task_id)

    elif args.action == 'mark-done':
        print(args.task_id)

    elif args.action == 'list':
        print(args.filter)
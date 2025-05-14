import task.services.id_checker as id_checker
import json
import time


def mark(args, file):
    '''Mark task as in progress or done'''
    id = args.task_id

    if id_checker.is_in_range(args.task_id, file):
        with open(file, 'r+') as tasks_json:
            # Load data from tasks.json
            tasks = json.load(tasks_json)
            # Update the task status and time stamp
            tasks['tasks'][id - 1]['status'] = args.action[5:]
            tasks['tasks'][id - 1]['updatedAt'] = time.asctime()

            # Go to the top of the tasks.json
            tasks_json.seek(0)

            # Overwrite the tasks.json with updated data
            json.dump(tasks, tasks_json, indent=4)

            # Remove trailing data
            tasks_json.truncate()

            print('Task (ID: {}) marked as {}'.format(id, args.action[5:]))
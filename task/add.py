import json
import time


def add(description, file):
    '''Add new task'''
    id = 1

    with open(file, 'r+') as tasks_json:
        # Load data from tasks.json
        tasks = json.load(tasks_json)

        # Check if tasks.json has any tasks
        if tasks['tasks']:
            # Increment the id by the last id
            id += tasks['tasks'][-1].get('id')

        # Append the new task to the old_tasks
        tasks['tasks'].append({
            'id': id,
            'description': description,
            'status': 'todo',
            'createdAt': time.asctime(),
            'updatedAt': time.asctime()
        })

        # Go to the top of the tasks.json
        tasks_json.seek(0)

        # Overwrite the tasks.json with new data
        json.dump(tasks, tasks_json, indent=4)

        print('Task added successfully (ID: {})'.format(id))
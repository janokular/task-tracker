import json
import time


def add(description: str, file):
    '''Add a new task'''
    id = 1

    with open(file, 'r+') as tasks_json:
        tasks = json.load(tasks_json)

        # Calculate ID for a new task
        if tasks['tasks']:
            id += tasks['tasks'][-1]['id']

        tasks['tasks'].append({
            'id': id,
            'description': description,
            'status': 'todo',
            'createdAt': time.asctime(),
            'updatedAt': time.asctime()
        })

        tasks_json.seek(0)

        json.dump(tasks, tasks_json, indent=4)

    print(f'Task added successfully (ID: {id})')

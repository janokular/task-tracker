import json
import time


def add(args, file):
    '''Add new task'''
    id = 1

    with open(file, 'r+') as tasks:
        # Load data from tasks.json
        old_tasks = json.load(tasks)

        # Check if tasks.json has any tasks
        if old_tasks['tasks']:
            # Increment the id by the last id
            id += old_tasks['tasks'][-1].get('id')

        # Append the new task to the old_tasks
        old_tasks['tasks'].append({
            'id': id,
            'description': args.task,
            'status': 'todo',
            'createdAt': time.asctime(),
            'updatedAt': time.asctime()
        })
        tasks.seek(0)

        # Overwrite the tasks.json with new data
        json.dump(old_tasks, tasks, indent=4)

        print('Task added successfully (ID: {})'.format(id))
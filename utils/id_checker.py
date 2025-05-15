import json
import sys


def is_in_range(id, file):
    '''Check if task id is in range'''
    ids = []

    # Load data form tasks.json
    with open(file) as tasks:
        tasks = json.load(tasks)

        # Append the task id to ids list
        for task in tasks['tasks']:
            ids.append(task['id'])

    if not ids:
        print('No tasks to delete')
        sys.exit(1)
    elif id < 1:
        print('(ID: {}) cannot be lower than 1'.format(id))
        sys.exit(1)
    elif id > ids[-1]:
        print('(ID: {}) is out of range, max value (ID: {})'.format(id, ids[-1]))
        sys.exit(1)
    else:
        return id in ids

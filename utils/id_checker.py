import json
import sys


def is_in_range(id, file):
    '''Check if task id is in range'''
    ids = []

    with open(file) as tasks:
        tasks = json.load(tasks)

        for task in tasks['tasks']:
            ids.append(task['id'])

    if not ids:
        print('No tasks to delete')
        sys.exit(1)
    elif id < 1:
        print(f'(ID: {id}) cannot be lower than 1')
        sys.exit(1)
    elif id > ids[-1]:
        print(f'(ID: {id}) is out of range, max value (ID: {ids[-1]})')
        sys.exit(1)
    else:
        return id in ids

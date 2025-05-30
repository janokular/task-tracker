import json


def is_in_range(id, file):
    '''Check if task id is in range'''
    ids = []

    with open(file) as tasks:
        tasks = json.load(tasks)

        for task in tasks['tasks']:
            ids.append(task['id'])

    if not ids:
        raise Exception('No tasks to delete')
    elif id < 1:
        raise Exception(f'(ID: {id}) cannot be lower than 1')
    elif id > ids[-1]:
        raise Exception(f'(ID: {id}) is out of range, max value (ID: {ids[-1]})')
    else:
        return id in ids

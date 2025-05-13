import json


def is_in_range(id, file):
    '''Check if task id is in range'''
    ids = []

    with open(file) as tasks:
        tasks = json.load(tasks)

        for task in tasks['tasks']:
            ids.append(task.get('id'))

    if id <= 0:
        print('(ID: {}) cannot be lower than 1'.format(id))
        return False
    elif id > ids[-1]:
        print('(ID: {}) is out of range, max value (ID: {})'.format(id, ids[-1]))
        return False
    else:
        return id in ids

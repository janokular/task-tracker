import json


def is_in_range(id, file):
    '''Check if task id is in range'''
    with open(file) as tasks:
        tasks = json.load(tasks)

        for task in tasks['tasks']:
            if id == task['id']:
                return True

        print(f'(ID: {id}) is out of range')
        return False

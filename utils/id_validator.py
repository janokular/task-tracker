import json


def is_id_in_range(id: int, file):
    '''Check if task id is in range'''
    with open(file) as tasks:
        tasks = json.load(tasks)

        for task in tasks['tasks']:
            if id == task['id']:
                return True

        print(f'error: (ID: {id}) is out of range')
        return False

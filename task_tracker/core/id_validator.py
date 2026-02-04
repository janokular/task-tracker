import json


RED = '\033[31m'
RESET = '\033[0m'


def id_validator(id: int, file):
    '''Check if task id is in range'''
    with open(file) as tasks:
        tasks = json.load(tasks)

        for task in tasks['tasks']:
            if id == task['id']:
                return True

        print(f'{RED}error: (ID: {id}) is out of range{RESET}')
        return False

import json


RED = '\033[31m'
RESET = '\033[0m'


def id_validator(id: int, filepath: str) -> bool:
    '''Check if task id is in range'''
    with open(filepath) as file:
        tasks = json.load(file)

        for task in tasks:
            if id == task['id']:
                return True

        print(f'{RED}error: No task with (ID: {id}) inside {filepath}{RESET}')
        return False

import json
from utils.table_print import add_row, display


def list(status: str, file):
    '''List all tasks or list them by status'''
    with open(file) as tasks_json:
        # Load data form tasks.json
        tasks = json.load(tasks_json)
        
        # Loop thorught tasks
        for task in tasks['tasks']:
            print(type(task))
            if status == None:
                add_row(task)
            # Filter lisiting based on task status
            elif status == task.get('status'):
                add_row(task)

        display()

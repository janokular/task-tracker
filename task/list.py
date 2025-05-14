import json


def list(status, file):
    '''List tasks'''
    with open(file) as tasks_json:
        # Load data form tasks.json
        tasks = json.load(tasks_json)
        
        # Loop thorught tasks
        for task in tasks['tasks']:
            if status == None:
                print(task)
            # Filter lisiting based on task status
            elif status == task.get('status'):
                print(task)
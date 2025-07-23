import json
from utils.table_print import print_table


def list(status: str, file):
    '''List all tasks or list them by status'''
    tasks_for_listing = []

    with open(file) as tasks_json:
        # Load data form tasks.json
        tasks = json.load(tasks_json)
        
        # Loop thorught tasks
        for task in tasks['tasks']:
            if status == None:
                tasks_for_listing.append(task)
            # Filter lisiting based on task status
            elif status == task.get('status'):
                tasks_for_listing.append(task)
    
    if tasks_for_listing:
        print_table(tasks_for_listing)

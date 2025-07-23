import json
from utils.table_print import print_table


def list(status: str, file):
    '''List all tasks or list them by status'''
    tasks_for_listing = []

    with open(file) as tasks_json:
        tasks = json.load(tasks_json)
        
        for task in tasks['tasks']:
            if status == None or status == task.get('status'):
                tasks_for_listing.append(task)
    
    if tasks_for_listing:
        print_table(tasks_for_listing)

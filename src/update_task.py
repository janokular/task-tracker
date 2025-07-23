import json
import time
from utils.id_validator import is_id_in_range


def update(id, action, updated_data, file):
    '''Update task'''
    if is_id_in_range(id, file):
        with open(file, 'r+') as tasks_json:
            # Load data from tasks.json
            tasks = json.load(tasks_json)

            # Check if user wants to updated status or description
            if action == 'update':
                tasks['tasks'][id - 1]['description'] = updated_data
            else:
                tasks['tasks'][id - 1]['status'] = updated_data
            tasks['tasks'][id - 1]['updatedAt'] = time.asctime()

            # Go to the top of the tasks.json
            tasks_json.seek(0)

            # Overwrite the tasks.json with updated data
            json.dump(tasks, tasks_json, indent=4)
            
            # Remove trailing data
            tasks_json.truncate()

            print(f'Task (ID: {id}) successfully updated')

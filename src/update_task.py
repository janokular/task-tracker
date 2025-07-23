import json
import time
from utils.id_validator import is_id_in_range


def update(id: int, action, updated_data: str, file):
    '''Update task's description or status'''
    if is_id_in_range(id, file):
        with open(file, 'r+') as tasks_json:
            tasks = json.load(tasks_json)

            if action == 'update':
                tasks['tasks'][id - 1]['description'] = updated_data
            else:
                tasks['tasks'][id - 1]['status'] = updated_data
            tasks['tasks'][id - 1]['updatedAt'] = time.asctime()

            tasks_json.seek(0)

            json.dump(tasks, tasks_json, indent=4)
            
            tasks_json.truncate()

        print(f'Task (ID: {id}) successfully updated')

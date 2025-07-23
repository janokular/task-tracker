import json
import time
from utils.id_validator import is_id_in_range


def update(id: int, action, updated_data: str, file):
    '''Update task's description or status'''
    if is_id_in_range(id, file):
        with open(file, 'r+') as tasks_json:
            tasks = json.load(tasks_json)

            for task in tasks['tasks']:
                if task['id'] == id:
                    if action == 'update':
                        task['description'] = updated_data
                    else:
                        task['status'] = updated_data
                task['updatedAt'] = time.asctime()

            tasks_json.seek(0)

            json.dump(tasks, tasks_json, indent=4)
            
            tasks_json.truncate()

        print(f'Task (ID: {id}) successfully updated')

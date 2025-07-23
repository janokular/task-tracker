import json
from utils.id_validator import is_id_in_range


def delete(id: int, file):
    '''Delete a task'''
    if is_id_in_range(id, file):
        with open(file, 'r+') as tasks_json:
            tasks = json.load(tasks_json)

            for task in tasks['tasks']:
                if task['id'] == id:
                    tasks['tasks'].remove(task)

            # Adjust ID's
            for task in tasks['tasks'][id - 1:]:
                task['id'] -= 1

            tasks_json.seek(0)

            json.dump(tasks, tasks_json, indent=4)

            tasks_json.truncate()

        print(f'Task (ID: {id}) deleted sucessfully')

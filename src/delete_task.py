import json
from utils.id_validator import is_id_in_range


def delete(id: int, file):
    '''Delete task'''
    if is_id_in_range(id, file):
        with open(file, 'r+') as tasks_json:
            # Load data from tasks.json
            tasks = json.load(tasks_json)

            # Delete task
            del tasks['tasks'][id - 1]

            # Decrement all id's after deleted task
            for task in tasks['tasks'][id - 1:]:
                task['id'] -= 1

            # Go to the top of the tasks.json
            tasks_json.seek(0)

            # Overwrite the tasks.json
            json.dump(tasks, tasks_json, indent=4)

            # Remove trailing data
            tasks_json.truncate()

            print(f'Task (ID: {id}) deleted sucessfully')

import utils.id_checker as id_checker
import json
import time


def add(description, file):
    '''Add new task'''
    id = 1

    with open(file, 'r+') as tasks_json:
        # Load data from tasks.json
        tasks = json.load(tasks_json)

        # Check if tasks.json has any tasks
        if tasks['tasks']:
            # Increment the new task id by the last task id
            id += tasks['tasks'][-1]['id']

        # Append the new task to the old_tasks
        tasks['tasks'].append({
            'id': id,
            'description': description,
            'status': 'todo',
            'createdAt': time.asctime(),
            'updatedAt': time.asctime()
        })

        # Go to the top of the tasks.json
        tasks_json.seek(0)

        # Overwrite the tasks.json with new data
        json.dump(tasks, tasks_json, indent=4)

        print('Task added successfully (ID: {})'.format(id))


def update(id, action, updated_data, file):
    '''Update task'''
    if id_checker.is_in_range(id, file):
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

            print('Task (ID: {}) successfully updated'.format(id))


def delete(id, file):
    '''Delete task'''
    if id_checker.is_in_range(id, file):
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

            print('Task (ID: {}) deleted sucessfully'.format(id))


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

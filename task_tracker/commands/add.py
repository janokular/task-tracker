import json

from ..core.file_service import get_file
from ..core.time_service import get_time


def add(description: str):
    '''Add a new task'''
    FILE = get_file()

    new_id = 1

    with open(FILE, 'r+') as tasks_json:
        tasks = json.load(tasks_json)

        # Calculate ID for a new task
        if tasks['tasks']:
            new_id += tasks['tasks'][-1]['id']

        tasks['tasks'].append(
            {
                'id': new_id,
                'description': description,
                'status': 'todo',
                'createdAt': get_time(),
                'updatedAt': get_time()
            }
        )

        tasks_json.seek(0)

        json.dump(tasks, tasks_json, indent=4)

    print(f'Task added successfully (ID: {new_id})')


def run(args):
    add(args.description)


def register(subparsers):
    add_parser = subparsers.add_parser(
        'add',
        help='add a new task',
    )
    add_parser.add_argument(
        'description',
        type=str,
        help='task description',
    )
    add_parser.set_defaults(func=run)

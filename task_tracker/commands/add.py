import json

from ..core.file_service import get_filepath
from ..core.time_service import get_time


def add(description: str):
    '''Add a new task'''
    filepath = get_filepath()
    new_id = 1

    with open(filepath, 'r+') as file:
        tasks = json.load(file)

        if tasks:
            new_id += tasks[-1]['id']

        tasks.append(
            {
                'id': new_id,
                'description': description,
                'status': 'todo',
                'createdAt': get_time(),
                'updatedAt': get_time()
            }
        )

        file.seek(0)

        json.dump(tasks, file, indent=4)

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

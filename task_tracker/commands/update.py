import json

from ..core.file_service import get_file
from ..core.id_validator import id_validator
from ..core.time_service import get_time


def update(id: int, description: str):
    '''Update task's description'''
    FILE = get_file()

    if id_validator(id, FILE):
        with open(FILE, 'r+') as tasks_json:
            tasks = json.load(tasks_json)

            for task in tasks['tasks']:
                if task['id'] == id:
                    task['description'] = description
                    task['updatedAt'] = get_time()

            tasks_json.seek(0)

            json.dump(tasks, tasks_json, indent=4)
            
            tasks_json.truncate()

        print(f'Task (ID: {id}) successfully updated')


def run(args):
    update(args.id, args.description)


def register(subparsers):
    update_parser = subparsers.add_parser(
        'update',
        help='update a task'
    )
    update_parser.add_argument(
        'id',
        type=int,
        help='task id',
    )
    update_parser.add_argument(
        'description',
        type=str,
        help='task description',
    )
    update_parser.set_defaults(func=run)

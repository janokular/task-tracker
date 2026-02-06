import json

from ..core.file_service import get_filepath
from ..core.id_validator import id_validator
from ..core.time_service import get_time


def update(id: int, description: str):
    '''Update task's description'''
    filepath = get_filepath()

    if id_validator(id, filepath):
        with open(filepath, 'r+') as file:
            tasks = json.load(file)

            for task in tasks:
                if task['id'] == id:
                    task['description'] = description
                    task['updatedAt'] = get_time()

            file.seek(0)

            json.dump(tasks, file, indent=4)
            
            file.truncate()

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

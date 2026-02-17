import json

from ..core.id_validator import id_validator
from ..core.file_service import get_filepath


def delete(id: int):
    '''Delete a task'''
    filepath = get_filepath()

    if id_validator(id, filepath):
        with open(filepath, 'r+') as file:
            tasks = json.load(file)

            for task in tasks:
                if task['id'] == id:
                    tasks.remove(task)

            file.seek(0)

            json.dump(tasks, file, indent=4)

            file.truncate()

        print(f'Task (ID: {id}) deleted successfully')


def run(args):
    delete(args.id)


def register(subparsers):
    delete_parser = subparsers.add_parser(
        'delete',
        help='delete a task'
    )
    delete_parser.add_argument(
        'id',
        type=int,
        help='task id',
    )
    delete_parser.set_defaults(func=run)

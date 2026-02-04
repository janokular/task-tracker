import json

from ..core.id_validator import id_validator
from ..core.file_service import get_file


def delete(id: int):
    '''Delete a task'''
    FILE = get_file()

    if id_validator(id, FILE):
        with open(FILE, 'r+') as tasks_json:
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

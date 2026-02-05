import json

from ..core.file_service import get_file
from ..core.id_validator import id_validator
from ..core.time_service import get_time


def mark_in_progress(id: int):
    '''Mark task as in-progress'''
    FILE = get_file()
    STATUS_MSG = 'in-progress'

    if id_validator(id, FILE):
        with open(FILE, 'r+') as tasks_json:
            tasks = json.load(tasks_json)

            for task in tasks['tasks']:
                if task['id'] == id:
                    task['status'] = STATUS_MSG
                    task['updatedAt'] = get_time()

            tasks_json.seek(0)

            json.dump(tasks, tasks_json, indent=4)
            
            tasks_json.truncate()

        print(f'Task (ID: {id}) marked as {STATUS_MSG}')


def run(args):
    mark_in_progress(args.id)


def register(subparsers):
    mark_in_progress_parser = subparsers.add_parser(
        'mark-in-progress',
        help='mark task as in progress',
    )
    mark_in_progress_parser.add_argument(
        'id',
        type=int,
        help='task id',
    )
    mark_in_progress_parser.set_defaults(func=run)

import json

from ..core.file_service import get_file
from ..core.id_validator import id_validator
from ..core.time_service import get_time


def mark_done(id: int):
    '''Mark task as done'''
    FILE = get_file()

    if id_validator(id, FILE):
        with open(FILE, 'r+') as tasks_json:
            tasks = json.load(tasks_json)

            for task in tasks['tasks']:
                if task['id'] == id:
                    task['status'] = 'done'
                    task['updatedAt'] = get_time()

            tasks_json.seek(0)

            json.dump(tasks, tasks_json, indent=4)
            
            tasks_json.truncate()

        print(f'Task (ID: {id}) marked as done')


def run(args):
    mark_done(args.id)


def register(subparsers):
    mark_done_parser = subparsers.add_parser(
        'mark-done',
        help='mark task as done',
    )
    mark_done_parser.add_argument(
        'id',
        type=int,
        help='task id',
    )
    mark_done_parser.set_defaults(func=run)

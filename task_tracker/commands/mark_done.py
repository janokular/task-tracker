import json

from ..core.file_service import get_filepath
from ..core.id_validator import id_validator
from ..core.time_service import get_time


def mark_done(id: int):
    '''Mark task as done'''
    filepath = get_filepath()
    status = 'done'

    if id_validator(id, filepath):
        with open(filepath, 'r+') as file:
            tasks = json.load(file)

            for task in tasks:
                if task['id'] == id:
                    task['status'] = status
                    task['updatedAt'] = get_time()

            file.seek(0)

            json.dump(tasks, file, indent=4)
            
            file.truncate()

        print(f'Task (ID: {id}) marked as {status}')


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

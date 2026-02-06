import json

from ..core.file_service import get_filepath
from ..core.id_validator import id_validator
from ..core.time_service import get_time


def mark_in_progress(id: int):
    '''Mark task as in-progress'''
    filepath = get_filepath()
    status = 'in-progress'

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

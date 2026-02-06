import json

from ..core.print_service import table
from ..core.file_service import get_filepath


def list(status: str):
    '''List all tasks or list them by status'''
    filepath = get_filepath()
    tasks_for_listing = []

    with open(filepath) as file:
        tasks = json.load(file)
        
        for task in tasks:
            if status == None or status == task.get('status'):
                tasks_for_listing.append(task)
    
    if tasks_for_listing:
        table(tasks_for_listing)
    else:
        print('No tasks for listing')


def run(args):
    list(args.status)


def register(subparsers):
    list_parser = subparsers.add_parser(
        'list',
        help='list tasks'
    )
    list_parser.add_argument(
        'status',
        nargs='?',
        choices=['done', 'todo', 'in-progress'],
        help='list tasks based on status'
    )
    list_parser.set_defaults(func=run)

import json

from ..core.print_service import table
from ..core.file_service import get_file


def list(status: str):
    '''List all tasks or list them by status'''
    FILE = get_file()

    tasks_for_listing = []

    with open(FILE) as tasks_json:
        tasks = json.load(tasks_json)
        
        for task in tasks['tasks']:
            if status == None or status == task.get('status'):
                tasks_for_listing.append(task)
    
    if tasks_for_listing:
        table(tasks_for_listing)


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

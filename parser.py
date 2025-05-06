import argparse

def parse_arguments():
    '''Parse arguments needed for program logic'''
    parser = argparse.ArgumentParser(description='Program used to track and manage your tasks')

    subparsers = parser.add_subparsers(dest='action')

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('task')

    update_parser = subparsers.add_parser('update', help='Update a task')
    update_parser.add_argument('task_id', type=int)
    update_parser.add_argument('task')

    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('task_id', type=int)

    mark_in_progress_parser = subparsers.add_parser('mark-in-progress', help='Mark task as in progress')
    mark_in_progress_parser.add_argument('task_id')

    mark_done_parser = subparsers.add_parser('mark-done', help='Mark task as done')
    mark_done_parser.add_argument('task_id', type=int)

    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('filter', nargs='?', choices=['done', 'todo', 'in-progress'])

    return parser.parse_args()
import argparse


def parse_arguments():
    '''Parse arguments needed for the program's logic'''
    parser = argparse.ArgumentParser(description='Program used to track and manage your tasks')

    subparsers = parser.add_subparsers(dest='action')

    add_parser = subparsers.add_parser('add', help='add a new task')
    add_parser.add_argument('description', type=str)

    delete_parser = subparsers.add_parser('delete', help='delete a task')
    delete_parser.add_argument('id', type=int)

    list_parser = subparsers.add_parser('list', help='list tasks')
    list_parser.add_argument('status', nargs='?', choices=['done', 'todo', 'in-progress'])

    mark_done_parser = subparsers.add_parser('mark-done', help='mark task as done')
    mark_done_parser.add_argument('id', type=int)

    mark_in_progress_parser = subparsers.add_parser('mark-in-progress', help='mark task as in progress')
    mark_in_progress_parser.add_argument('id', type=int)

    update_parser = subparsers.add_parser('update', help='update a task')
    update_parser.add_argument('id', type=int)
    update_parser.add_argument('description', type=str)

    args = parser.parse_args()

    return args if args.action else parser.error('No arguments provided')

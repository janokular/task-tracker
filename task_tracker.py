#!/bin/env python3


import utils.file_checker as file_checker
import utils.parser as parser
import src.task as task


def main():
    FILE = 'tasks.json'

    # Create a new file if not existing or empty
    file_checker.create_if_missing(FILE)

    # Parse arguments from a user
    args = parser.parse_arguments()

    # Handle passed arguments
    match args.action:
        case 'add':
            task.add(args.task_description, FILE)
        case 'update':
            task.update(args.task_id, args.action, args.task_description, FILE)
        case 'mark-in-progress':
            task.update(args.task_id, args.action, 'in-progress', FILE)
        case 'mark-done':
            task.update(args.task_id, args.action, 'done', FILE)
        case 'delete':
            task.delete(args.task_id, FILE)
        case 'list':
            task.list(args.task_status, FILE)
        case _:
            print('Something went wrong')

if __name__ == '__main__':
    main()

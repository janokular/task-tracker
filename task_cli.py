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
    if args.action == 'add':
        task.add(args.task_description, FILE)

    elif args.action == 'update':
        task.update(args.task_id, args.task_description, FILE)

    elif args.action == 'delete':
        task.delete(args.task_id, FILE)

    elif args.action == 'mark-in-progress':
        task.mark(args.task_id, 'in-progress', FILE)

    elif args.action == 'mark-done':
        task.mark(args.task_id, 'done', FILE)

    elif args.action == 'list':
        task.list(args.task_status, FILE)

if __name__ == '__main__':
    main()
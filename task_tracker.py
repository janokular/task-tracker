#!/bin/env python3


from utils.file_service import create_file
from utils.parser import parse_arguments
from src.add_task import add
from src.update_task import update
from src.delete_task import delete
from src.list_tasks import list


def main():
    FILE = 'tasks.json'

    create_file(FILE)

    args = parse_arguments()

    match args.action:
        case 'add':
            add(args.task_description, FILE)
        case 'update':
            update(args.task_id, args.action, args.task_description, FILE)
        case 'mark-in-progress':
            update(args.task_id, args.action, 'in-progress', FILE)
        case 'mark-done':
            update(args.task_id, args.action, 'done', FILE)
        case 'delete':
            delete(args.task_id, FILE)
        case 'list':
            list(args.task_status, FILE)
        case _:
            print('error: Something went wrong')

if __name__ == '__main__':
    main()

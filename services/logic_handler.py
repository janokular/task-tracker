import task.add as add
import task.update as update
import task.delete as delete
import task.mark as mark
import task.list as list


def handle(args, file):
    '''Handle the program logic'''
    if args.action == 'add':
        add.add(args.task_description, file)

    elif args.action == 'update':
        update.update(args.task_id, args.task_description, file)

    elif args.action == 'delete':
        delete.delete(args.task_id, file)

    elif args.action == 'mark-in-progress':
        mark.mark(args.task_id, 'in-progress', file)

    elif args.action == 'mark-done':
        mark.mark(args.task_id, 'done', file)

    elif args.action == 'list':
        list.list(args.task_status, file)
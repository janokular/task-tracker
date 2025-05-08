import task.add as add
import task.update as update
import task.delete as delete
import task.list as list


def handle(args, file):
    '''Handle the program logic'''
    if args.action == 'add':
        add.add(args, file)

    elif args.action == 'update':
        update.update(args, file)

    elif args.action == 'delete':
        delete.delete(args, file)

    elif args.action == 'mark-in-progress':
        update.mark(args, file)

    elif args.action == 'mark-done':
        update.mark(args, file)

    elif args.action == 'list':
        list.list(args, file)
import add
import update
import delete
import list


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
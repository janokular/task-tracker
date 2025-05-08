import json


def list(args, file):
    '''List tasks'''
    with open(file) as tasks:
        tasks = json.load(tasks)
        
        for task in tasks['tasks']:
            if args.status == None:
                print(task)
            elif args.status == task.get('status'):
                print(task)
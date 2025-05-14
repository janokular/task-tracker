import json


def list(args, file):
    '''List tasks'''
    with open(file) as tasks_json:
        # Load data form tasks.json
        tasks = json.load(tasks_json)
        
        # Loop thorught tasks
        for task in tasks['tasks']:
            if args.status == None:
                print(task)
            # Apply filter if user provided args.status
            elif args.status == task.get('status'):
                print(task)
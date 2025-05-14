import task.services.id_checker as id_checker
import json


def delete(args, file):
    '''Delete task'''
    if id_checker.is_in_range(args.task_id, file):
        print(args.task_id)
        print('in range')
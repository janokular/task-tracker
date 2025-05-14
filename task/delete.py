import task.services.id_checker as id_checker
import json


def delete(id, file):
    '''Delete task'''
    if id_checker.is_in_range(id, file):
        print(id)
        print('in range')
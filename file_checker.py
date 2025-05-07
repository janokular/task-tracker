import os
import json


def create_if_missing(file):
    '''Check if tasks.json file exists and is not empty'''
    if not os.path.exists(file) or os.path.getsize(file) == 0:
        with open(file, 'w') as tasks:
            json.dump({"tasks": []}, tasks)
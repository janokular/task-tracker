import os
import json


def create_file(file):
    '''Create JSON file if file is missing or if it is empty'''
    if not os.path.exists(file) or os.path.getsize(file) == 0:
        with open(file, 'w') as tasks:
            json.dump({"tasks": []}, tasks)

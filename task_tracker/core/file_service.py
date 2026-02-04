import os
import json


def get_file():
    '''Create JSON file if file is missing or if it is empty'''
    FILE = 'tasks.json'

    if not os.path.exists(FILE) or os.path.getsize(FILE) == 0:
        with open(FILE, 'w') as tasks:
            json.dump({"tasks": []}, tasks)
    
    return FILE

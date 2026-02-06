import os
import json


FILEPATH = 'tasks.json'


def get_filepath() -> str:
    '''Get tasks.json filepath'''
    filepath_validator(FILEPATH)
    return FILEPATH


def filepath_validator(filepath: str):
    '''Create JSON file if filepath does not exist or file is empty'''
    if (
        not os.path.exists(filepath)
        or os.path.getsize(filepath) == 0
    ):
        with open(filepath, 'w') as file:
            json.dump([], file)

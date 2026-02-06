import time


def get_time() -> str:
    '''Get current time'''
    return time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())

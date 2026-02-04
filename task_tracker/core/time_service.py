import time


def get_time():
    '''Get current time'''
    return time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())

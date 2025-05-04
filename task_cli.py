#!/bin/env python3

# Program used to track and manage your tasks

import sys
import argparse
import json

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Program used to track and manage your tasks')

    parser.add_argument('add')
    parser.add_argument('update')
    parser.add_argument('delete')
    parser.add_argument('mark-in-progress')
    parser.add_argument('mark-done')
    parser.add_argument('list')

    args = parser.parse_args()
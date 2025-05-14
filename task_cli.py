#!/bin/env python3

import services.parser as parser
import services.file_checker as file_checker
import services.logic_handler as logic_handler


def main():
    FILE = 'tasks.json'

    # Parse arguments from a user
    args = parser.parse_arguments()

    # Create a new file if not existing or empty
    file_checker.create_if_missing(FILE)

    # Handle passed arguments
    logic_handler.handle(args, FILE)

if __name__ == '__main__':
    main()
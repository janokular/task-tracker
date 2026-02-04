import argparse

from .commands import add
from .commands import delete
from .commands import list
from .commands import mark_done
from .commands import mark_in_progress
from .commands import update


def build_parser():
    parser = argparse.ArgumentParser(
        prog='task_tracker',
        description='Task Tracker - track and manage your tasks',
    )
    subparsers = parser.add_subparsers(
        dest='command'
    )

    add.register(subparsers)
    delete.register(subparsers)
    list.register(subparsers)
    mark_done.register(subparsers)
    mark_in_progress.register(subparsers)
    update.register(subparsers)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

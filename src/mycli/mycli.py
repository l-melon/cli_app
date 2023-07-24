import argparse
from .commands import EasyCommand

def patched_main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    EasyCommand(subparsers)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()
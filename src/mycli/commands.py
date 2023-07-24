from abc import ABC, abstractmethod


class Command:
    pass

class EasyCommand(Command):
    def __init__(self, subparser) -> None:
        self.parser = subparser.add_parser("easy", help="easy command")
        self.parser.add_argument('echo', help='echo the string you use here')
        self.parser.set_defaults(func=self.run)
    
    def run(self, args):
        print(args)
        print(args.echo)

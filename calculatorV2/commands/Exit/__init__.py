import sys
from calculatorV2.commands import Command


class ExitCommand(Command):
    def execute(self):
        sys.exit("Exiting...")
from calculatorV2.commands import Command

class MenuCommand(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self):
        commands = self.command_handler.get_commands()
        print("Available commands:", "\t\t".join(commands))
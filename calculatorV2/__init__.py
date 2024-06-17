
from calculatorV2.commands import CommandHandler
from calculatorV2.commands.Addition import AdditionCommand
from calculatorV2.commands.Exit import ExitCommand


class Calculator:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    def start(self):
        # List of Commands
        self.command_handler.register_command("add", AdditionCommand())

        self.command_handler.register_command("exit", ExitCommand())


        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").strip())
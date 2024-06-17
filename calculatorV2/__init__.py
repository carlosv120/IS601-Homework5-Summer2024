
from calculatorV2.commands import CommandHandler
from calculatorV2.commands.Addition import AdditionCommand
from calculatorV2.commands.Division import DivisionCommand
from calculatorV2.commands.Exit import ExitCommand
from calculatorV2.commands.Menu import MenuCommand
from calculatorV2.commands.Multiplication import MultiplicationCommand
from calculatorV2.commands.Subtraction import SubtractionCommand


class Calculator:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    def start(self):
        # List of Commands
        self.command_handler.register_command("add", AdditionCommand())
        self.command_handler.register_command("subtract", SubtractionCommand())
        self.command_handler.register_command("multiply", MultiplicationCommand())
        self.command_handler.register_command("divide", DivisionCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))

        # Print available commands
        self.command_handler.execute_command("menu")

        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").strip())
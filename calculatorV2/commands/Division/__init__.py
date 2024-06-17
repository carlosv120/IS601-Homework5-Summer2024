from decimal import Decimal, InvalidOperation
from calculatorV2.commands import Command

class DivisionCommand(Command):
    def execute(self, num1=None, num2=None, raise_exception=False):
        try:
            if num1 is None:
                num1 = input("Enter the first number: ").strip()
            if num2 is None:
                num2 = input("Enter the second number: ").strip()

            if raise_exception:
                raise Exception("Forced exception for testing")

            num1_decimal, num2_decimal = map(Decimal, [num1, num2])

            if num2_decimal == 0:
                raise ValueError("Cannot divide by zero")

            result = num1_decimal / num2_decimal

            print(f"The result of dividing {num1_decimal} by {num2_decimal} is: {result}")

        except InvalidOperation:
            print(f"Invalid number input: {num1} or {num2} is not a valid number. You are in the main menu.")
        
        except ValueError as ve:
            print(ve)
            raise ve
        
        except Exception as e:
            print(f"An error occurred: {e}")

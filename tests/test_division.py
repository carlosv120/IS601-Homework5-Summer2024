'''Testing DivisionCommand'''
import pytest
from calculatorV2.commands.Division import DivisionCommand

def test_divide_success(capfd):
    """Test the division command with valid inputs."""
    command = DivisionCommand()
    command.execute('6', '3')
    out = capfd.readouterr().out
    assert out.strip() == "The result of dividing 6 by 3 is: 2"

def test_divide_invalid_number(capfd):
    """Test the division command with one valid and one invalid input."""
    command = DivisionCommand()
    command.execute('1.1', 'abc')
    out = capfd.readouterr().out
    assert out.strip() == "Invalid number input: 1.1 or abc is not a valid number. You are in the main menu."

def test_divide_user_input_prompts(monkeypatch, capfd):
    """Test the division command prompts for user input when num1 and num2 are None."""
    inputs = iter(['6', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = DivisionCommand()
    command.execute()
    out = capfd.readouterr().out
    assert out.strip() == "The result of dividing 6 by 2 is: 3"

def test_divide_by_zero():
    """Testing the divide by zero"""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command = DivisionCommand()
        command.execute('10', '0')

def test_divide_generic_exception(capfd):
    """Test the division command with a forced generic exception."""
    command = DivisionCommand()
    command.execute('6', '3', raise_exception=True)
    out = capfd.readouterr().out
    assert "An error occurred: Forced exception for testing" in out.strip()

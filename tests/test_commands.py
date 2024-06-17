"""Tests for calculatorV2 Commands"""
from calculatorV2.commands.Addition import AdditionCommand

def test_add(capfd):
    """Test the addition command."""
    command = AdditionCommand()
    command.execute()
    out = capfd.readouterr()
    assert out.out.strip() == "Hello, World!", "The AdditionCommand should print 'Hello, World!'"

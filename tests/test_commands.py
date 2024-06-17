"""Tests for calculatorV2 Commands"""
import pytest
from calculatorV2.commands.Addition import AdditionCommand
from calculatorV2.commands import Command

def test_add(capfd):
    """Test the addition command."""
    command = AdditionCommand()
    command.execute()
    out = capfd.readouterr()
    assert out.out.strip() == "Hello, World!", "The AdditionCommand should print 'Hello, World!'"

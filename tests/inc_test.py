""" content of calculator.py#"""
import pytest
from calculator.main import Calculator

def test_calc_add():
    """ Test the addition function """
    calc = Calculator()
    calc.add_number(1)
    assert calc.result == 7

def test_calc_subtract():
    """ Test the subtraction function """
    calc = Calculator()
    calc.subtract_number(1)
    assert calc.result == 5

# Change result in main.py to properly test multiplication
def test_calc_multiply():
    """ Test the multiplication function """
    calc = Calculator()
    calc.multiply_number(4)
    assert calc.result == 24

def test_calc_divide():
    """ Test the division function """
    calc = Calculator()
    calc.divide_number(2)
    assert calc.result == 3

def test_calc_divide_zero():
    """ Tests division by zero """
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide_number(0)

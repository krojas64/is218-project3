""" content of calc.py#"""
import pytest
from calc.calculator import Calculator

#import Addition in separate addition test file

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

# Change result in calculator.py to properly test multiplication
def test_calc_multiply():
    """ Test the multiplication function """
    calc = Calculator()
    calc.multiply_number(4)
    assert calc.result == 24

    #assert Calculator.multiply_numbers

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

def test_calculator_history_static_property():
    """ Testing static addition """
    Calculator.add_numbers(1,2)
    assert len(Calculator.history) == 1

def test_calculator_history_getAdditionCalculation():
    """ Testing static history """
    calculation = Calculator.history(0)
    assert calculation.getResult() == 3

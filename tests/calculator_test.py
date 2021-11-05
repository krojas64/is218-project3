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

def test_calculator_history_get_addition_calculation():
    """ Testing static history """
    calculation = Calculator.history[0]
    assert calculation.get_result() == 3

def test_calculator_history_length():
    """ Get the amount of items in the history """
    history_count = Calculator.get_history_length()
    assert history_count == 1

def test_remove_item_history():
    """ Removes a value from history """
    calculation = Calculator.history[0]
    Calculator.remove_item_history(calculation)
    new_history_count = Calculator.get_history_length()
    assert new_history_count == 0

def test_clear_history():
    """ Test the clear history function """
    Calculator.add_numbers(1,2)
    Calculator.subtract_numbers(5,1)
    Calculator.multiply_numbers(3,5)
    Calculator.divide_numbers(20,4)
    Calculator.clear_history()
    clear_test = Calculator.get_history_length()
    assert clear_test == 0

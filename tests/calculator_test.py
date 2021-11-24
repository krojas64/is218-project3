""" content of calc.py#"""

from calc.calculator import Calculator

#import Addition in separate addition test file

def test_calculator_history_static_property():
    """ Testing static addition """
    numbers = (1.0,2.0)
    Calculator.add_numbers(numbers)
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
    numbers1 = (1.0,2.0)
    numbers2 = (5.0, 1.0)
    numbers3 = (3.0,5.0)
    numbers4 = (20.0,4.0)
    Calculator.add_numbers(numbers1)
    Calculator.subtract_numbers(numbers2)
    Calculator.multiply_numbers(numbers3)
    Calculator.divide_numbers(numbers4)
    Calculator.clear_history()
    clear_test = Calculator.get_history_length()
    assert clear_test == 0

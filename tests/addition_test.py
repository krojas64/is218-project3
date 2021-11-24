""" Testing Addition """
from calc.operations.addition import Addition

def test_calculation_addition():
    """ Testing calculator static addition method """
    numbers = (3.0,4.0)
    addition = Addition(numbers)
    assert addition.get_result() == 7.0

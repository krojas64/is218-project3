""" Testing Addition """
from calc.calculations.addition import Addition

def test_calculation_addition():
    """ Testing calculator static addition method """
    addition = Addition(1,2)
    result = addition.getResult()
    assert result == 3

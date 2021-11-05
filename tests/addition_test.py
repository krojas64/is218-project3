""" Testing Addition """
from calc.operations.addition import Addition

def test_calculation_addition():
    """ Testing calculator static addition method """
    addition = Addition(1,2)
    result = addition.get_result()
    assert result == 3

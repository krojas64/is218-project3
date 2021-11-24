""" Testing multiplication """

from calc.operations.multiplication import Multiplication

def test_multiplication():
    """ Testing calculation of multiplication """
    numbers = (5.0, 3.0)
    multiply = Multiplication(numbers)
    assert multiply.get_result() == 15.0

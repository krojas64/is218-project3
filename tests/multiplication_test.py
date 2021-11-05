""" Testing multiplication """

from calc.operations.multiplication import Multiplication

def test_multiplication():
    """ Testing calculation of multiplication """
    multiplication = Multiplication(4,3)
    result = multiplication.get_result()
    assert result == 12

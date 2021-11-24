""" Testing subtraction """

from calc.operations.subtraction import Subtraction

def test_subtraction():
    """ Testing calculation of subtraction """
    numbers = (5.0, 1.0)
    subtraction = Subtraction(numbers)
    assert subtraction.get_result() == -6.0

""" Testing subtraction """

from calc.operations.subtraction import Subtraction

def test_subtraction():
    """ Testing calculation of subtraction """
    subtraction = Subtraction(6,2)
    result = subtraction.getResult()
    assert result == 4
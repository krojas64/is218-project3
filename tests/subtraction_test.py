""" Testing subtraction """

from calc.operations.subtraction import Subtraction

def test_subtraction():
    """ Testing calculation of subtraction """
    subtraction = Subtraction(6,2)
    result = subtraction.get_result()
    assert result == 4

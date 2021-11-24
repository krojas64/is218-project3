""" Testing division """

from calc.operations.division import Division

def test_division():
    """ Testing calculation of division """
    numbers = (4.0, 2.0)
    division = Division(numbers)
    assert division.get_result() == 0.125

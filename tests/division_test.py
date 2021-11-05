""" Testing division """

from calc.operations.division import Division

def test_division():
    """ Testing calculation of division """
    division = Division(15,3)
    result = division.get_result()
    assert result == 5

# pylint: disable=too-few-public-methods
""" Division Class """
from calc.operations.calculation import Calculation

class Division(Calculation):
    """ Division function """

    def get_result(self):
        """ Get result from division of values """
        result = 1.0
        for value in self.values:
            result = result / value
        return result

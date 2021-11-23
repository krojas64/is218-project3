# pylint: disable=too-few-public-methods
""" Subtraction Class """
from calc.operations.calculation import Calculation

class Subtraction(Calculation):
    """ Subtraction function """

    def get_result(self):
        """ Get difference of values from tuple """
        difference = 0.0
        for value in self.values:
            difference = difference - value
        return difference

# pylint: disable=too-few-public-methods
""" Multiplication Class """
from calc.operations.calculation import Calculation

class Multiplication(Calculation):
    """ Multiplication function """

    def get_result(self):
        """ Get multiplication result of values from tuple """
        result = 1.0
        for value in self.values:
            result = result * value
        return result

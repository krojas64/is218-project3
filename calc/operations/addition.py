# pylint: disable=too-few-public-methods
""" Addition Class """
from calc.operations.calculation import Calculation

class Addition(Calculation):
    """ Addition function """
    def get_result(self):
        """ Sum values from tuple """
        summation = 0.0
        for value in self.values:
            summation = summation + value
        return summation

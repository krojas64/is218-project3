# pylint: disable=too-few-public-methods
""" Multiplication Class """
from calc.operations.calculation import Calculation

class Multiplication(Calculation):
    """ Multiplication function """

    def get_result(self):
        """ Get result """
        return self.value_a * self.value_b

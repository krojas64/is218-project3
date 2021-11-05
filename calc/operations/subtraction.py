""" Subtraction Class """
from calc.operations.calculation import Calculation

class Subtraction(Calculation):
    """ Subtraction function """

    def get_result(self):
        """ Get result """
        return self.value_a - self.value_b

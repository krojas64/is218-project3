# pylint: disable=too-few-public-methods
""" Division Class """
from calc.operations.calculation import Calculation

class Division(Calculation):
    """ Division function """

    def get_result(self):
        """ Get result """
        return self.value_a / self.value_b

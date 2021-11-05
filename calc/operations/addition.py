""" Addition Class """
from calc.operations.calculation import Calculation

class Addition(Calculation):
    """ Addition function """
    def get_result(self):
        """ Get result """
        return self.value_a + self.value_b

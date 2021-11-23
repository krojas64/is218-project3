# pylint: disable=too-few-public-methods
""" Calculation Class """

class Calculation:
    """ Class used to pass onto other functions """
    # default constructor
    def __init__(self, values: tuple):
        """ Constructor """
        self.values = Calculation.convert_to_float(values)

    @staticmethod
    def convert_to_float(values):
        """ Converts values to floats """
        floats = []
        for number in values:
            floats.append(float(number))
        return floats
""" Calculation Class """

class Calculation:

    # default constructor
    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b

    # Class factory method
    @classmethod
    def create(cls, value_a, value_b):
        return cls(value_a, value_b)
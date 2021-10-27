""" This is the Calculator function"""

class Calculator:
    """ Calculator func """
    result = 6
    def add_number(self, value_a):
        """ Add value_a to the result """
        self.result = self.result + value_a
        return self.result

    def subtract_number(self, value_b):
        """ Subtract value_b from the result """
        self.result = self.result - value_b
        return self.result

    def multiply_number(self, value_c):
        """ Multiply value_c with the result """
        self.result = self.result * value_c
        return self.result

    def divide_number(self, value_d):
        """ Divide the result by value_d """
        if value_d == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        self.result = self.result / value_d
        return self.result

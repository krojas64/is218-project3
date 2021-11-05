""" This is the Calculator function """
#Add calculator.py to new folder called calculator
#Maybe put all tests under calculator test (?)
from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division

class Calculator:
    """ Calculator func """
    history = []

    @staticmethod
    def clear_history():
        """ Clears the history """
        Calculator.history.clear()
        return True

    @staticmethod
    def remove_item_history(value_a):
        Calculator.history.remove(value_a)
        return True

    result = 6
    def add_number(self, value_a):
        """ Add value_a to the result """
        self.result = self.result + value_a
        return self.result

    @staticmethod
    def add_numbers(value_a, value_b):
        """ Add numbers and get result """
        addition = Addition(value_a, value_b)
        Calculator.history.append(addition)
        return addition.getResult

    def subtract_number(self, value_b):
        """ Subtract value_b from the result """
        self.result = self.result - value_b
        return self.result

    @staticmethod
    def subtract_numbers(value_a, value_b):
        """ Subtract numbers and get result """
        subtraction = Subtraction(value_a, value_b)
        Calculator.history.append(subtraction)
        return subtraction.getResult

    def multiply_number(self, value_c):
        """ Multiply value_c with the result """
        self.result = self.result * value_c
        return self.result

    # Figure out what to add to make this work
    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply numbers and store result """
        Calculator.add_calculation_to_history(Multiplication.create(value_a, value_b))
        return Calculator.get_result_of_last_calculation_added_to_history

    def divide_number(self, value_d):
        """ Divide the result by value_d """
        if value_d == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        self.result = self.result / value_d
        return self.result

    @staticmethod
    def divide_numbers(value_a, value_b):
        """ Divide numbers and get result """
        division = Division(value_a, value_b)
        Calculator.history.append(division)
        return division.getResult
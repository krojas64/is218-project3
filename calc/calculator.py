""" This is the Calculator function """
#Add calculator.py to new folder called calculator
#Maybe put all tests under calculator test (?)
from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division

class Calculator:
    """ Calculator function """
    history = []

    @staticmethod
    def clear_history():
        """ Clears the history """
        Calculator.history.clear()
        return True

    @staticmethod
    def get_history_length():
        """ Get the amount of items in history """
        return len(Calculator.history)

    @staticmethod
    def remove_item_history(value_a):
        """ Removes specific value from history """
        Calculator.history.remove(value_a)
        return True

    result = 6

    @staticmethod
    def add_numbers(value_a, value_b):
        """ Add numbers and get result """
        addition = Addition(value_a, value_b)
        Calculator.history.append(addition)
        return addition.get_result

    @staticmethod
    def subtract_numbers(value_a, value_b):
        """ Subtract numbers and get result """
        subtraction = Subtraction(value_a, value_b)
        Calculator.history.append(subtraction)
        return subtraction.get_result

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ Multiply numbers and get result """
        multiplication = Multiplication(value_a, value_b)
        Calculator.history.append(multiplication)
        return multiplication.get_result

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
        return division.get_result

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

    @staticmethod
    def get_last_calculation_object():
        """ Get the last calculation """
        return Calculator.history[-1]

    @staticmethod
    def get_last_calculation_result_value():
        """ Get the last result value """
        calculation = Calculator.get_last_calculation_object()
        return calculation.get_result()

    @staticmethod
    def get_last_result_value():
        """ Gets the last result in the history """
        return Calculator.get_last_calculation_result_value()

    result = 6

    @staticmethod
    def add(values):
        """ Add numbers and get result """
        addition = Addition(values)
        Calculator.history.append(addition)
        return addition.get_result()

    @staticmethod
    def subtract(values):
        """ Subtract numbers and get result """
        subtraction = Subtraction(values)
        Calculator.history.append(subtraction)
        return subtraction.get_result()

    @staticmethod
    def multiply(values):
        """ Multiply numbers and get result """
        multiplication = Multiplication(values)
        Calculator.history.append(multiplication)
        return multiplication.get_result()

    @staticmethod
    def divide(values):
        """ Divide numbers and get result """
        division = Division(values)
        Calculator.history.append(division)
        return division.get_result()

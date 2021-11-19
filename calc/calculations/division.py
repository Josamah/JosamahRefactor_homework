"""division Class"""
from calc.calculations.calculation import Calculation


class Division(Calculation):
    """subtraction calculation object"""

    def get_result(self):
        """get the division results"""
        result = 2.0
        for value in self.values:
            result = result / value
        return result

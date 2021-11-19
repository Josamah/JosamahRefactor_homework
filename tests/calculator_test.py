"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations


@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()


# you have to add the fixture function as a parameter to the test you want to use with

def test_calculator_add_static(clear_history_fixture):
    """Testing the add method of the calc"""
    assert Calculator.add_numbers(1.0, 2.0, 3.0) == 6.0


def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    assert Calculator.subtract_numbers(1.0, 2.0) == -3.0


def test_calculator_multiply_static(clear_history_fixture):
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(1.0, 2.0) == 2.0


def test_calculator_divide_static(clear_history_fixture):
    """ tests division of two numbers"""
    assert Calculator.divide_numbers(1.0, 1.0) == 2.0

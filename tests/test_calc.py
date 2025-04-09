from src.calc import Calculator
import pytest

calc  = Calculator()

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (4, 3, 7),
        (-2, 8, 6),
        (0, 0, 0),
    ]
)
def test_sum(a, b, expected):
    assert calc.sum(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (4, 3, 1),
        (-2, 8, -10),
        (0, 0, 0),
    ]
)
def test_subtract(a, b, expected):
    assert calc.subtract(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (4, 3, 12),
        (-2, 8, -16),
        (1, 1, 1),
    ]
)
def test_multiply(a, b, expected):
    assert calc.multiply(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (4, 2, 2),
        (-8, 2, -4),
        (1, 1, 1),
    ]
)
def test_divide(a, b, expected):
    assert calc.divide(a, b) == expected
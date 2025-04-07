from src.calc import Calculator

calc  = Calculator()

def test_addition():
    assert calc.sum(2, 2) == 4
    assert calc.sum(-2, 2) == 0
    assert calc.sum(2, -3) == -1
    assert calc.sum(2, 2.5) == 4.5
    assert calc.sum(2, 2/2) == 3.0

def test_subtract():
    assert calc.subtract(2, 2) == 0
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(2, -3) == 5
    assert calc.subtract(2, 2.5) == -0.5
    assert calc.subtract(2, 2/2) == 1.0

def test_multiply():
    assert calc.multiply(2, 2) == 4
    assert calc.multiply(5, 3) == 15
    assert calc.multiply(2, -3) == -6
    assert calc.multiply(2, 2.5) == 5
    assert calc.multiply(2, 2/2) == 2.0

def test_divide():
    assert calc.divide(2, 2) == 1
    assert calc.divide(5, 2) == 2.5
    assert calc.divide(2, -4) == -0.5
    assert calc.divide(2, 2.5) == 0.8
    assert calc.divide(2, 2/2) == 2.0
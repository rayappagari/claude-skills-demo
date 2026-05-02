import pytest
from app import add, divide


def test_add_basic_cases():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_add_float_and_negative_cases():
    assert add(1.5, 2.5) == 4.0
    assert add(-5, -3) == -8


def test_divide_basic_cases():
    assert divide(10, 2) == 5.0
    assert divide(-10, 2) == -5.0
    assert divide(10, -2) == -5.0


def test_divide_float_precision():
    assert divide(1, 3) == pytest.approx(0.333, rel=1e-3)


def test_divide_by_zero_message():
    with pytest.raises(ValueError, match="divisor cannot be zero"):
        divide(5, 0)
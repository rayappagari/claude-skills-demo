import pytest
from app import add, divide


def test_add_floats():
    assert add(1.5, 2.5) == 4.0


def test_add_negative_numbers():
    assert add(-5, -3) == -8


def test_divide_negative_numbers():
    assert divide(-10, 2) == -5.0
    assert divide(10, -2) == -5.0


def test_divide_by_zero_message():
    with pytest.raises(ValueError, match="divisor cannot be zero"):
        divide(5, 0)
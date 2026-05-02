import pytest
from app import add, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(1, 3) == pytest.approx(0.333, rel=1e-3)


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
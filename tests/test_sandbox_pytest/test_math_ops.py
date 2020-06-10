import pytest
from sandbox_pytest.math_ops import add, div, multiply, sub


@pytest.fixture()
def test_ints():
    return 1, 2, 3, 4


def test_add(test_ints) -> None:
    assert add(test_ints) == 10


def test_sub(test_ints) -> None:
    assert sub(test_ints) == -8


def test_multiply(test_ints) -> None:
    assert multiply(test_ints) == 24


def test_div() -> None:
    assert div((4, 2, 1)) == 2

import pytest
from sandbox_pytest.math_ops import add, div, multiply, sub


@pytest.fixture()
def test_ints():
    return 1, 2, 3, 4


@pytest.fixture()
def test_list():
    return [1, 2, 3, 4]


def test_add_tuple(test_ints) -> None:
    assert add(test_ints) == 10


def test_add_list(test_list) -> None:
    assert add(test_list) == 10


def test_sub_tuple(test_ints) -> None:
    assert sub(test_ints) == -8


def test_multiply_tuple(test_ints) -> None:
    assert multiply(test_ints) == 24


def test_div_tuple() -> None:
    assert div((4, 2, 1)) == 2

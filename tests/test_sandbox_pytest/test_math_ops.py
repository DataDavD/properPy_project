import pytest
from sandbox_pytest.math_ops import add, div, multiply, sub


@pytest.fixture()
def test_ints_tuple():
    return 1, 2, 3, 4


@pytest.fixture()
def test_list():
    return [1, 2, 3, 4]


@pytest.mark.tuple
def test_add_tuple(test_ints_tuple) -> None:
    assert add(test_ints_tuple) == 10


def test_add_list(test_list) -> None:
    assert add(test_list) == 10


def test_add_ints() -> None:
    assert add(1, 2, 3, 4) == 10


@pytest.mark.tuple
def test_sub_tuple(test_ints_tuple) -> None:
    assert sub(test_ints_tuple) == -8


def test_sub_list(test_list) -> None:
    assert sub(test_list) == -8


def test_sub_ints() -> None:
    assert sub(1, 2, 3, 4) == -8


@pytest.mark.tuple
def test_multiply_tuple(test_ints_tuple) -> None:
    assert multiply(test_ints_tuple) == 24


def test_multiply_list(test_list) -> None:
    assert multiply(test_list) == 24


def test_multiply_ints() -> None:
    assert multiply(1, 2, 3, 4) == 24


@pytest.mark.tuple
def test_div_tuple() -> None:
    assert div((4, 2, 1)) == 2


def test_div_list() -> None:
    assert div([4, 2, 1]) == 2


def test_div_ints() -> None:
    assert div(4, 2, 1) == 2

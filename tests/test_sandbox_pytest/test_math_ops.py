from typing import List, Tuple

import pytest

from sandbox_pytest.math_ops import add, div, multiply, sub


@pytest.fixture()
def test_ints_tuple() -> Tuple[int, ...]:
    return 1, 2, 3, 4


@pytest.fixture()
def test_list() -> List[int]:
    return [1, 2, 3, 4]


@pytest.mark.tuple
def test_add_tuple(test_ints_tuple) -> None:
    assert add(test_ints_tuple) == 10


def test_add_list(test_list) -> None:
    assert add(test_list) == 10


def test_add_ints() -> None:
    assert add(1, 2, 3, 4) == 10


@pytest.mark.parametrize(
    "add_args, add_exp_result", [((1, 2, 3, 4), 10), ([1, 2, 3, 4], 10), ((2, 3, 5), 10)]
)
def test_add_params_ints(add_args, add_exp_result) -> None:
    assert add(*add_args) == add_exp_result


@pytest.mark.parametrize(
    "add_args, add_exp_result", [((1, 2, 3, 4), 10), ([1, 2, 3, 4], 10), ((2, 3, 5), 10)]
)
def test_add_params_iterables(add_args, add_exp_result) -> None:
    assert add(add_args) == add_exp_result


@pytest.mark.tuple
def test_sub_tuple(test_ints_tuple) -> None:
    assert sub(test_ints_tuple) == -8


def test_sub_list(test_list) -> None:
    assert sub(test_list) == -8


def test_sub_ints() -> None:
    assert sub(1, 2, 3, 4) == -8


@pytest.mark.parametrize(
    "add_args, add_exp_result", [((10, 5), 5), ([100, 100, 0, 5], -5), ((500, 100, 300), 100)]
)
def test_sub_params_ints(add_args, add_exp_result) -> None:
    assert sub(*add_args) == add_exp_result


@pytest.mark.parametrize(
    "add_args, add_exp_result", [((10, 5), 5), ([100, 100, 0, 5], -5), ((500, 100, 300), 100)]
)
def test_sub_params_iterables(add_args, add_exp_result) -> None:
    assert sub(add_args) == add_exp_result


@pytest.mark.tuple
def test_multiply_tuple(test_ints_tuple) -> None:
    assert multiply(test_ints_tuple) == 24


def test_multiply_list(test_list) -> None:
    assert multiply(test_list) == 24


def test_multiply_ints() -> None:
    assert multiply(1, 2, 3, 4) == 24


@pytest.mark.parametrize(
    "add_args, add_exp_result",
    [((10, 5), 50), ([100, 100, 0, 5], 0), ((500, 100, 300), 15_000_000)],
)
def test_multiply_params_iterables(add_args, add_exp_result) -> None:
    assert multiply(*add_args) == add_exp_result


@pytest.mark.parametrize(
    "add_args, add_exp_result",
    [((10, 5), 50), ([100, 100, 0, 5], 0), ((500, 100, 300), 15_000_000)],
)
def test_multiply_params_ints(add_args, add_exp_result) -> None:
    assert multiply(add_args) == add_exp_result


@pytest.mark.tuple
def test_div_tuple() -> None:
    assert div((4, 2, 1)) == 2


def test_div_list() -> None:
    assert div([4, 2, 1]) == 2


def test_div_ints() -> None:
    assert div(4, 2, 1) == 2


@pytest.mark.parametrize(
    "add_args, add_exp_result", [((10, 5), 2), ([100, 100, 1], 1), ((500, 250), 2)],
)
def test_div_params_iterables(add_args, add_exp_result) -> None:
    assert div(*add_args) == add_exp_result


@pytest.mark.parametrize(
    "add_args, add_exp_result", [((10, 5), 2), ([100, 100, 1], 1), ((500, 250), 2)],
)
def test_div_params_ints(add_args, add_exp_result) -> None:
    assert div(add_args) == add_exp_result

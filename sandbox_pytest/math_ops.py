from functools import reduce
from typing import Sequence, Union


def add(*args: Union[Sequence[int], int]) -> int:
    if all(isinstance(x, int) for x in args):
        result = reduce((lambda x, y: x + y), args)  # type: ignore
        return result  # type: ignore
    else:
        result = reduce((lambda x, y: x + y), *args)  # type: ignore
        return result  # type: ignore


def sub(*args: Union[Sequence[int], int]) -> int:
    if all(isinstance(x, int) for x in args):
        result = reduce((lambda x, y: x - y), args)  # type: ignore
        return result  # type: ignore
    else:
        result = reduce((lambda x, y: x - y), *args)  # type: ignore
        return result  # type: ignore


def multiply(*args: Union[Sequence[int], int]) -> int:
    if all(isinstance(x, int) for x in args):
        result = reduce((lambda x, y: x * y), args)  # type: ignore
        return result  # type: ignore
    else:
        result = reduce((lambda x, y: x * y), *args)  # type: ignore
        return result  # type: ignore


def div(*args: Union[Sequence[int], int]) -> int:
    if all(isinstance(x, int) for x in args):
        result = reduce((lambda x, y: x / y), args)  # type: ignore
        return result  # type: ignore
    else:
        result = reduce((lambda x, y: x / y), *args)  # type: ignore
        return result  # type: ignore

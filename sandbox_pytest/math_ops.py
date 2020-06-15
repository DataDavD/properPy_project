def add(*args: int) -> int:
    result: int = args[0]
    for x in args[1:]:
        result += x
    return result


def sub(*args: int) -> int:
    result: int = args[0]
    for x in args[1:]:
        result -= x
    return result


def multiply(*args: int) -> int:
    result: int = args[0]
    for x in args[1:]:
        result *= x
    return result


def div(*args: int) -> float:
    result: float = args[0]
    for x in args[1:]:
        result /= x
    return result

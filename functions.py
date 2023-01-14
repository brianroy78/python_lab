from functools import partial
from typing import Callable


def compose(*functions: Callable) -> Callable:
    if len(functions) == 0:
        def nothing(param):
            return param

        return nothing

    def compose_(param):
        result = param
        for func in functions:
            result = func(result)
        return result

    return compose_


def filtrate(function) -> Callable:
    return partial(filter, function)


def mapper(function) -> Callable:
    return partial(map, function)


def if_else(bool_func, true_value, false_value, value):
    return true_value if bool_func(value) else false_value


def is_empty(value) -> bool:
    return len(value) == 0

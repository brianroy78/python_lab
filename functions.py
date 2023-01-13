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

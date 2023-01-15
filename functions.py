from dataclasses import dataclass

import functools as ft
import typing as ty


def compose(*functions: ty.Callable) -> ty.Callable:
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


InputValue = ty.TypeVar('InputValue')
OutputValue = ty.TypeVar('OutputValue')

InputIterator = ty.Iterator[InputValue]
OutputIterator = ty.Iterator[OutputValue]

InputFiltrate = ty.Callable[[InputValue], bool]
OutputFiltrate = ty.Callable[[InputIterator], InputIterator]


def filtrate(function: InputFiltrate) -> OutputFiltrate:
    return ft.partial(filter, function)


InputMapper = ty.Callable[[InputValue], OutputValue]
OutputMapper = ty.Callable[[InputIterator], OutputIterator]


def mapper(function: InputMapper) -> OutputMapper:
    return ft.partial(map, function)


def if_else(bool_func, true_value, false_value, value):
    return true_value if bool_func(value) else false_value


def is_empty(value: ty.Union[str, list, dict, tuple]) -> bool:
    return len(value) == 0


@dataclass
class Premise:
    expected: ty.Any
    result: ty.Any


def switch_case(default: ty.Any, premises: list[Premise], value: ty.Any):
    for p in premises:
        if p.expected == value:
            return p.result
    return default

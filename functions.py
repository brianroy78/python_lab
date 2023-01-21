import typing as ty
from dataclasses import dataclass


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

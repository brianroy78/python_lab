import functools as ft
import itertools as it
import operator as op

import functions as f
import functors as fu

count_parentheses = ft.partial(
    f.switch_case, 0, (f.Premise("(", 1), f.Premise(")", -1))
)


def main_logic(length, counts):
    return (
        fu.IterFunctor(it.islice(counts, length - 1))
        .map(ft.partial(op.le, 0))
        .flat(all)
        .apply(ft.partial(op.and_, next(counts) == 0))
    ).value


def valid_parentheses(string: str) -> bool:
    if f.is_empty(string):
        return True
    return (
        fu.IterFunctor(string)
        .map(count_parentheses)
        .accumulate(op.add)
        .flat(ft.partial(main_logic, len(string)))
        .value
    )


print(valid_parentheses("  ("), False, "should work for '  ('")
print(valid_parentheses(")test"), False, "should work for ')test'")
print(valid_parentheses(""), True, "should work for ''")
print(valid_parentheses("hi())("), False, "should work for 'hi())('")
print(valid_parentheses("hi(hi)()"), True, "should work for 'hi(hi)()'")

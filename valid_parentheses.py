import functools as ft
import itertools as it
import operator as op

import functions as f

is_valid = ft.partial(op.le, 0)
count_parentheses = ft.partial(f.switch_case, 0, (f.Premise('(', 1), f.Premise(')', -1)))


def main_logic(length, counts):
    others = it.islice(counts, length - 1)
    are_valid = f.compose(f.mapper(is_valid), all)
    return are_valid(others) and next(counts) == 0


def valid_parentheses(string):
    if f.is_empty(string):
        return True
    return f.compose(
        f.mapper(count_parentheses),
        ft.partial(it.accumulate, func=op.add),
        ft.partial(main_logic, len(string))
    )(string)


print(valid_parentheses("  ("), False, "should work for '  ('")
print(valid_parentheses(")test"), False, "should work for ')test'")
print(valid_parentheses(""), True, "should work for ''")
print(valid_parentheses("hi())("), False, "should work for 'hi())('")
print(valid_parentheses("hi(hi)()"), True, "should work for 'hi(hi)()'")


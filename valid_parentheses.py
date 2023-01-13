from functools import partial
from itertools import accumulate

import functions as funcs
import operator as op


def is_p(char):
    return char in ('(', ')')


def count_p(char):
    return 1 if char == '(' else -1


def is_valid(count):
    return count < 0


def valid_parentheses(string):
    if len(string) == 0:
        return True

    return funcs.compose(
        funcs.filtrate(is_p),
        funcs.mapper(count_p),
        partial(accumulate, func=op.add),
        funcs.mapper(is_valid),
        all
    )



print(valid_parentheses("  ("), False, "should work for '  ('")
print(valid_parentheses(")test"), False, "should work for ')test'")
print(valid_parentheses(""), True, "should work for ''")
print(valid_parentheses("hi())("), False, "should work for 'hi())('")
print(valid_parentheses("hi(hi)()"), True, "should work for 'hi(hi)()'")

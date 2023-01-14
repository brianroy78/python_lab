from functools import partial
from itertools import accumulate

import functions as funcs
import operator as op

OPEN_PARENTHESIS = '('
PARENTHESES = (OPEN_PARENTHESIS, ')')

is_a_parenthesis = partial(op.contains, PARENTHESES)
is_open_parenthesis = partial(op.eq, OPEN_PARENTHESIS)
count_parenthesis = partial(funcs.if_else, is_open_parenthesis, 1, -1)


def main_logic(counts):
    last = 0
    for count in counts:
        if count == -1:
            return False
        last = count
    return last == 0


def valid_parentheses(string):
    if funcs.is_empty(string):
        return True

    return funcs.compose(
        funcs.filtrate(is_a_parenthesis),
        funcs.mapper(count_parenthesis),
        partial(accumulate, func=op.add),
        main_logic
    )(string)


print(valid_parentheses("  ("), False, "should work for '  ('")
print(valid_parentheses(")test"), False, "should work for ')test'")
print(valid_parentheses(""), True, "should work for ''")
print(valid_parentheses("hi())("), False, "should work for 'hi())('")
print(valid_parentheses("hi(hi)()"), True, "should work for 'hi(hi)()'")

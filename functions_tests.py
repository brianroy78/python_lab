from functools import partial
from operator import add

from functions import compose


def test_happy_path():
    result = compose(int, partial(add, 2), str)('4')
    assert result == '6'


test_happy_path()

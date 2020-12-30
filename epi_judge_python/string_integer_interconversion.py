from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    # TODO - you fill in here.
    sign = ''
    if x == 0:
        return '0'
    elif x < 0:
        sign = "-"
        x = abs(x)
    ret = []
    while x:
        ret.append(chr(ord('0') + x % 10))
        x //= 10

    ret.append(sign)

    return "".join(reversed(ret))


def string_to_int(s: str) -> int:
    # TODO - you fill in here.
    start = 0
    sign = 1
    if s[0] == '-':
        sign = -1
        start = 1
    elif s[0] == '+':
        start = 1

    ret = 0
    for i in range(start, len(s)):
        ret = ret * 10 + ord(s[i]) - ord('0')
    return ret * sign


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))

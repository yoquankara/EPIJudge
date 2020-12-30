from test_framework import generic_test
import string


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # TODO - you fill in here.
    sign, start = '', 0
    if num_as_string[0] == '-':
        sign = '-'
        start = 1

    # Convert from b1 base to decimal base
    d = 0
    for i in range(start, len(num_as_string)):
        d = d * b1 + string.hexdigits.index(num_as_string[i].lower())

    # Convert to b2 base
    ret = []
    while d:
        ret.append(string.hexdigits[d % b2].upper())
        d //= b2
    if not ret:
        return '0'
    ret.append(sign)

    return ''.join(reversed(ret))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))

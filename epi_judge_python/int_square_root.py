from test_framework import generic_test


def square_root(k: int) -> int:
    # TODO - you fill in here.
    l, r, res = 0, k, -1
    while l <= r:
        m = l + (r-l)//2
        tmp = m**2
        if tmp > k:
            r = m - 1
        elif tmp < k:
            l = m + 1
            res = m
        else:
            return m
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))

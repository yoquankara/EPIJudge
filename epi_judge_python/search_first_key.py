from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    # TODO - you fill in here.
    l, r, res = 0, len(A)-1, -1
    while l <= r:
        m = l + (r-l)//2
        if A[m] < k:
            l = m + 1
        elif A[m] > k:
            r = m - 1
        else:
            r = m - 1
            res = m

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))

import bisect
from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    res = []
    # Method 1: one list is much longer than the other. O(nlogm) Ave: 3ms, median: 6us
    def is_in(a: int, B: List[int]):
        idx = bisect.bisect_left(B, a)
        return idx < len(B) and B[idx] == a

    if len(A) > len(B):
        A, B = B, A
    for a in A:
        if is_in(a, B) and a not in res:
            res.append(a)

#    # Method 2: both are same order of length.  O(n+m) Ave: 3ms, median: 8us
#    i, j = 0, 0
#    while i < len(A) and j < len(B):
#        if A[i] < B[j]:
#            i += 1
#        elif A[i] > B[j]:
#            j += 1
#        else:
#            if A[i] not in res:
#                res.append(A[i])
#            i += 1
#            j += 1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))

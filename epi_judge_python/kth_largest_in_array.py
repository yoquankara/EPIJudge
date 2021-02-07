import random
from typing import List

from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    # TODO - you fill in here.
    if k > len(A):
        raise ValueError("k is larger than list size")

    def partition_around_pivot(left, right, pivot_idx) -> int:
        """Find new pivot idx that A[left:new_pivot_dix] are all greater than pivot value,
        A[new_pivot_idx+1, right] are all less than pivot value"""
        pivot_value = A[pivot_idx]
        new_pivot_idx = left
        A[pivot_idx], A[right] = A[right], A[pivot_idx]
        for i in range(left, right):
            if A[i] > pivot_value:
                A[new_pivot_idx], A[i] = A[i], A[new_pivot_idx]
                new_pivot_idx += 1
        A[new_pivot_idx], A[right] = A[right], A[new_pivot_idx]
        return new_pivot_idx

    left, right = 0, len(A) - 1
    while left <= right:
        pivot_idx = random.randint(left, right)
        new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
        if new_pivot_idx == k - 1:
            return A[new_pivot_idx]
        elif new_pivot_idx < k - 1:
            left = new_pivot_idx + 1
        else:
            right = new_pivot_idx - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))

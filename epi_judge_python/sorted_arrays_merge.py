import heapq
from typing import List

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    # return list(heapq.merge(*sorted_arrays))
    ret = []
    sorted_arrays_iters = [iter(l) for l in sorted_arrays]
    min_heap = [(next(l), i) for i, l in enumerate(sorted_arrays_iters) if l]
    heapq.heapify(min_heap)
    while min_heap:
        min_val, idx = heapq.heappop(min_heap)
        ret.append(min_val)
        next_val = next(sorted_arrays_iters[idx], None)
        if next_val is not None:
            heapq.heappush(min_heap, (next_val, idx))

    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))

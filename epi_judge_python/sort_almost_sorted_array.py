import heapq
import itertools
from typing import Iterator, List

from test_framework import generic_test


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    # TODO - you fill in here.
    heap : List[int] = []
    res = []
    for s in itertools.islice(sequence, k):
        heapq.heappush(heap, s)

    for s in sequence:
        res.append(heapq.heappushpop(heap, s))

    while heap:
        res.append(heapq.heappop(heap))

    return res


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))

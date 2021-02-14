from typing import List, DefaultDict
from collections import defaultdict

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    str_to_pos: DefaultDict[str, int] = defaultdict()
    min_distance = float('inf')
    for i, p in enumerate(paragraph):
        if p in str_to_pos:
            min_distance = min(min_distance, i - str_to_pos[p])
        str_to_pos[p] = i
    return min_distance if min_distance < float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))

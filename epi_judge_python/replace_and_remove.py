import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    # TODO - you fill in here.
    # Forward pass, remove 'b' and count 'a'
    write_idx, a_cnt = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_cnt += 1

    curr = write_idx - 1
    write_idx += a_cnt - 1
    final_size = write_idx + 1

    # Backward pass, pre-compute
    while curr >= 0:
        if s[curr] == 'a':
            s[write_idx], s[write_idx-1] = 'd', 'd'
            write_idx -= 2
        else:
            s[write_idx] = s[curr]
            write_idx -= 1
        curr -= 1

    return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))

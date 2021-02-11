import collections
from typing import List, DefaultDict, Tuple

from test_framework import generic_test, test_utils


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    # O(nmlogm)
    signatures: DefaultDict[str, List[str]] = collections.defaultdict(list)
    for s in dictionary:
        signatures[''.join(sorted(s))].append(s)

    # O(nm)
    # signatures: DefaultDict[Tuple[int], List[str]] = collections.defaultdict(list)
    # for s in dictionary:
    #     k_u = [0] * 27
    #     k_p = [0] * 26
    #     for c in s:
    #         if c == ' ':
    #             k_u[-1] += 1
    #         elif c == c.lower():
    #             k_u[ord(c) - ord('a')] += 1
    #         else:
    #             k_p[ord(c) - ord('A')] += 1
    #     signatures[tuple(k_u + k_p)].append(s)
    return [group for group in signatures.values()
            if len(group) > 1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))

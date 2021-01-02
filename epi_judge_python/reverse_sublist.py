from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    # TODO - you fill in here.
    dummy_head = ListNode(0, L)

    prev = dummy_head

    # Find start node
    i = 1
    while prev and i < start:
        prev = prev.next
        i += 1
    if not prev or not prev.next:
        return None
    start_node = prev.next

    for _ in range(finish-start):
        tail = start_node.next

        start_node.next = tail.next
        tail.next = prev.next
        prev.next = tail

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))

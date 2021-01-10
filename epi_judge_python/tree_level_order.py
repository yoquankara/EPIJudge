from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    # TODO - you fill in here.
    ret = []
    if tree is None:
        return ret
    curr_level = [tree]

    # Shorter code but longer time
    #while curr_level:
    #    ret.append([n.data for n in curr_level])
    #    curr_level = [
    #        child for n in curr_level
    #        for child in (n.left, n.right) if child
    #    ]
    #return ret

    while curr_level:
        tmp = []
        next_level = []
        for n in curr_level:
            tmp.append(n.data)
            if n.left is not None:
                next_level.append(n.left)
            if n.right is not None:
                next_level.append(n.right)
        ret.append(tmp)
        curr_level = next_level

    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))

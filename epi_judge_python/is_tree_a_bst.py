from typing import Union

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    def in_order_tranverse(tree: BinaryTreeNode, last_max: float=float("-inf")) -> Union[float, None]:
        """Return current max data or None if not BST"""
        if tree.left:
            left_max = in_order_tranverse(tree.left, last_max)
            if left_max is None:
                return None
            last_max = max(last_max, left_max)
        if tree.data < last_max:
            return None
        if tree.right:
            return in_order_tranverse(tree.right, tree.data)
        else:
            return tree.data

    return tree is None or in_order_tranverse(tree) is not None


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))

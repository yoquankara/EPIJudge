from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    def height(t: BinaryTreeNode) -> int:
        """Return -1 if not balanced, otherwise return max child's height"""
        if not t:
            return 0
        l = height(t.left)
        if l == -1:
            return -1
        r = height(t.right)
        if r == -1 or abs(l-r) > 1:
            return -1
        return max(l, r) + 1

    return height(tree) > -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))

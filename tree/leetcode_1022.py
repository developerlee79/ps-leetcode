from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.sum_tree(root, 0)

    def sum_tree(self, root: Optional[TreeNode], prev: int) -> int:
        curr = (prev << 1) + root.val
        left = 0
        right = 0

        if not root.left and not root.right:
            return curr
        if root.left:
            left = self.sum_tree(root.left, curr)
        if root.right:
            right = self.sum_tree(root.right, curr)

        return left + right

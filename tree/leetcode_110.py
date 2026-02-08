from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.calculate_depth(root) != -1

    def calculate_depth(self, root) -> int:
        if not root:
            return 0

        left_depth = self.calculate_depth(root.left)
        if left_depth == -1:
            return -1

        right_depth = self.calculate_depth(root.right)
        if right_depth == -1:
            return -1

        if abs(left_depth - right_depth) > 1:
            return -1

        return 1 + max(left_depth, right_depth)

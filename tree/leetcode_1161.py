from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_level = -1
        max_level_sum = float('-inf')
        level = 1
        queue = [root]

        while queue:
            size = len(queue)
            level_sum = 0
            for _ in range(size):
                node = queue.pop(0)
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_sum > max_level_sum:
                max_level_sum = level_sum
                max_level = level
            level += 1

        return max_level
        
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def kthLargestLevelSum(self, root, k):
        queue = [root]

        levels = []

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

            levels.append(level_sum)

        if len(levels) < k:
            return -1

        return sorted(levels, reverse=True)[k - 1]

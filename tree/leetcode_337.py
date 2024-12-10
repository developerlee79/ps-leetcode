class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rob(self, root):
        optimal = self.find_optimal_money(root)
        return max(optimal)

    def find_optimal_money(self, root):
        if not root:
            return [0, 0]

        left = self.find_optimal_money(root.left)
        right = self.find_optimal_money(root.right)

        optimal = [
            max(left) + max(right),
            left[0] + right[0] + root.val
        ]

        return optimal

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        x_node = self.find_x(root, x)
        lefts = self.count_nodes(x_node.left)
        rights = self.count_nodes(x_node.right)
        roots = n - lefts - rights - 1
        return lefts + rights < roots or lefts + roots < rights or rights + roots < lefts

    def find_x(self, root, x):
        if not root or root.val == x:
            return root
        return self.find_x(root.left, x) or self.find_x(root.right, x)

    def count_nodes(self, root):
        if not root:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

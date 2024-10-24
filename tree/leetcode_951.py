class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flipEquiv(self, root1, root2):
        return self.is_equals(root1, root2)

    def is_equals(self, node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2 or node1.val != node2.val:
            return False

        left_equal = self.is_equals(node1.left, node2.left) or self.is_equals(node1.left, node2.right)
        right_equal = self.is_equals(node1.right, node2.right) or self.is_equals(node1.right, node2.left)

        return left_equal and right_equal

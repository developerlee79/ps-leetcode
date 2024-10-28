class Solution(object):
    def isUnivalTree(self, root):
        return self.is_unival(root.val, root)

    def is_unival(self, value, node):
        if not node:
            return True
        if node.val != value:
            return False
        return self.is_unival(value, node.left) and self.is_unival(value, node.right)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumEvenGrandparent(self, root):
        queue = [(root, -1, -1)]
        grandchild_sum = 0
        while queue:
            node, parent, grand_parent = queue.pop(0)
            if grand_parent & 1 == 0:
                grandchild_sum += node.val
            if node.left:
                queue.append((node.left, node.val, parent))
            if node.right:
                queue.append((node.right, node.val, parent))
        return grandchild_sum

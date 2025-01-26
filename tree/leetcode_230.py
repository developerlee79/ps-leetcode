class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def kthSmallest(self, root, k):
        nodes = []
        self.collect_nodes(root, nodes)
        nodes.sort()
        return nodes[k - 1]

    def collect_nodes(self, root, nodes):
        if not root:
            return
        nodes.append(root.val)
        self.collect_nodes(root.left, nodes)
        self.collect_nodes(root.right, nodes)

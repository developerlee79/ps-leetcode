class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def replaceValueInTree(self, root):
        queue = [root]
        root.val = 0

        while queue:
            depth_sum = 0
            node_sum = []

            for node in queue:
                leaf_sum = 0
                if node.left:
                    leaf_sum += node.left.val
                if node.right:
                    leaf_sum += node.right.val
                node_sum.append(leaf_sum)
                depth_sum += leaf_sum

            size = len(queue)

            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    node.left.val = depth_sum - node_sum[i]
                    queue.append(node.left)
                if node.right:
                    node.right.val = depth_sum - node_sum[i]
                    queue.append(node.right)

        return root

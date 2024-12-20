class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def reverseOddLevels(self, root):
        queue = [root]
        depth = 0

        while queue:
            size = len(queue)
            half_size = size >> 1
            arr = []
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)
                if depth & 1 == 1:
                    arr.append(node)
                    if i >= half_size:
                        self.swap(arr[i], arr[size - 1 - i])
            depth += 1

        return root

    @staticmethod
    def swap(node1, node2):
        node1.val, node2.val = node2.val, node1.val

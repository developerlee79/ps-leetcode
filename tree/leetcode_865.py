class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def subtreeWithAllDeepest(self, root):
        graph = {root: -1}
        levels = {}
        queue = [root]
        depth = 0

        while queue:
            size = len(queue)
            levels[depth] = []
            for _ in range(size):
                node = queue.pop(0)
                levels[depth].append(node)
                if node.left:
                    graph[node.left.val] = node
                    queue.append(node.left)
                if node.right:
                    graph[node.right.val] = node
                    queue.append(node.right)
            depth += 1

        leftmost = levels[depth - 1][0]
        rightmost = levels[depth - 1][-1]
        while leftmost != rightmost:
            leftmost = graph[leftmost.val]
            rightmost = graph[rightmost.val]
        return leftmost

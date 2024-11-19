class Solution(object):
    def findLeaves(self, root):
        leaves = []
        self.find_leaves(root, 0, leaves)
        return leaves

    def find_leaves(self, node, depth, leaves):
        if not node:
            return depth

        if not node.left and not node.right:
            if depth == len(leaves):
                leaves.append([])
            leaves[depth].append(node.val)
            return depth + 1

        left_depth = self.find_leaves(node.left, depth, leaves)
        right_depth = self.find_leaves(node.right, depth, leaves)

        current_depth = max(left_depth, right_depth)

        if current_depth == len(leaves):
            leaves.append([])

        leaves[current_depth].append(node.val)

        return current_depth + 1

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node_list = []

        def find_node_values(root: Optional[TreeNode]):
            if not root:
                return
            find_node_values(root.left)
            node_list.append(root.val)
            find_node_values(root.right)

        find_node_values(root)

        def build_balanced_tree(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            mid = (left + right) >> 1
            node = TreeNode(node_list[mid])

            node.left = build_balanced_tree(left, mid - 1)
            node.right = build_balanced_tree(mid + 1, right)

            return node

        return build_balanced_tree(0, len(node_list) - 1)

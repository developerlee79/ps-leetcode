class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution(object):
    def findRoot(self, tree):
        tree_map = {}

        for node in tree:
            if node.children:
                for c in node.children:
                    if c.val not in tree_map:
                        tree_map[c.val] = []
                    tree_map[c.val].append(node.val)

        for node in tree:
            if node.val not in tree_map:
                return node

        return None

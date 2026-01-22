from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0
        root = Node(-1)
        node_index = root

        for num in nums:
            node_index.next = Node(num)
            node_index = node_index.next

        while True:
            min_pair = float('inf')
            min_node = None
            is_sorted = True
            node_index = root.next

            while node_index.next is not None:
                curr_pair = node_index.data + node_index.next.data
                if curr_pair < min_pair:
                    min_pair = curr_pair
                    min_node = node_index
                if node_index.data > node_index.next.data:
                    is_sorted = False
                node_index = node_index.next

            if is_sorted:
                break

            min_node.data = min_pair
            min_node.next = min_node.next.next
            operations += 1

        return operations

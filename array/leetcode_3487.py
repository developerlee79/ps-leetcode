from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_sum = 0
        max_ele = float('-inf')
        is_added = False
        num_set = set()
        for num in nums:
            max_ele = max(max_ele, num)
            if num not in num_set and num > 0:
                max_sum += num
                is_added = True
            num_set.add(num)
        return max_sum if is_added else max_ele

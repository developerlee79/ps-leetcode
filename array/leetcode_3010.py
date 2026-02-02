from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min_a = float('inf')
        min_b = float('inf')

        for x in nums[1:]:
            if x < min_a:
                min_b = min_a
                min_a = x
            elif x < min_b:
                min_b = x

        return nums[0] + min_a + min_b

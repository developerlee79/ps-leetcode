from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = sum(nums)
        count = 0

        for i in range(n - 1):
            left += nums[i]
            right -= nums[i]
            count += 1 if left & 1 == right & 1 else 0

        return count

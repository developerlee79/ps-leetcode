from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        min_count = n - 1
        rightmost_idx = 0

        for i in range(n - 1):
            j = rightmost_idx
            while j < n and nums[i] * k >= nums[j]:
                j += 1
            min_count = min(min_count, i + (n - j))
            rightmost_idx = j

        return min_count

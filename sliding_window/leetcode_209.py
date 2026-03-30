from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr = 0
        min_len = float('inf')

        for i, num in enumerate(nums):
            curr += num
            while left <= i and curr >= target:
                min_len = min(min_len, i - left + 1)
                curr -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len

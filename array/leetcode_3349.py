from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        inc = 1
        prev_inc = 0
        max_len = 0

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc += 1
            else:
                prev_inc = inc
                inc = 1
            max_len = max(max_len, max(inc >> 1, min(prev_inc, inc)))
            if max_len >= k:
                return True

        return False

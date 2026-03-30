from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        min_dq = deque()
        max_dq = deque()

        for i, num in enumerate(nums):
            while min_dq and nums[min_dq[-1]] > num:
                min_dq.pop()
            while max_dq and nums[max_dq[-1]] < num:
                max_dq.pop()
            min_dq.append(i)
            max_dq.append(i)
            if nums[max_dq[0]] - nums[min_dq[0]] > limit:
                if left == max_dq[0]:
                    max_dq.popleft()
                if left == min_dq[0]:
                    min_dq.popleft()
                left += 1

        return len(nums) - left

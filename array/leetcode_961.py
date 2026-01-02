from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) >> 1
        target = -1
        count = 0
        for num in nums:
            if num != target:
                target = num
                count = 0
            count += 1
            if count >= n:
                break
        return target

from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num = nums[i]
            num_sum = 0
            while num > 0:
                num_sum += num % 10
                num //= 10
            if num_sum == i:
                return i

        return -1

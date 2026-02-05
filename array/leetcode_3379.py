from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        for i, num in enumerate(nums):
            if num == 0:
                result[i] = num
            elif num > 0:
                result[i] = nums[(i + num) % n]
            else:
                result[i] = nums[(i - abs(num)) % n]

        return result

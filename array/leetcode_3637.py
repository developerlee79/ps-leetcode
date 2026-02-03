from typing import List
from itertools import groupby


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        diffs = [(b > a) - (b < a) for a, b in zip(nums, nums[1:])]

        if 0 in diffs:
            return False

        return [k for k, _ in groupby(diffs)] == [1, -1, 1]

from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        directions = [[0] * 2 for _ in range(n)]
        i = 1
        j = n - 2
        while i < n:
            directions[i][0] = directions[i - 1][0] + nums[i - 1]
            directions[j][1] = directions[j + 1][1] + nums[j + 1]
            i += 1
            j -= 1
        for i, direction in enumerate(directions):
            if nums[i] != 0:
                continue
            left, right = direction
            if left == right:
                count += 2
            elif abs(left - right) == 1:
                count += 1
        return count

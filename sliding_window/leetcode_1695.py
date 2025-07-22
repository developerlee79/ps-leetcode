from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_score = 0
        score = 0
        num_set = set()
        i, j = 0, 0
        while i < n:
            if nums[j] in num_set:
                max_score = max(max_score, score)
                while i < j and nums[i] != nums[j]:
                    score -= nums[i]
                    num_set.remove(nums[i])
                    i += 1
                if nums[i] == nums[j]:
                    i += 1
            else:
                num_set.add(nums[j])
                score += nums[j]
            if j < n - 1:
                j += 1
        return max_score

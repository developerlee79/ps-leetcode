class Solution(object):
    def maxAdjacentDistance(self, nums):
        n = len(nums)
        answer = abs(nums[0] - nums[-1])
        for i in range(1, n):
            answer = max(abs(nums[i] - nums[i - 1]), answer)
        return answer

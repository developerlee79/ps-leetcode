class Solution(object):
    def maxAbsoluteSum(self, nums):
        n = len(nums)
        min_prefix = nums[0]
        max_prefix = nums[0]
        max_sum = abs(nums[0])
        for i in range(1, n):
            min_prefix = min(nums[i], nums[i] + min_prefix)
            max_prefix = max(nums[i], nums[i] + max_prefix)
            max_sum = max(max_sum, abs(min_prefix), max_prefix)
        return max(max_sum, 0)

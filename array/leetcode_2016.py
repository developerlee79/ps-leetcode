class Solution(object):
    def maximumDifference(self, nums):
        n = len(nums)
        max_diff = -1
        left = nums[0]
        for i in range(1, n):
            if nums[i] > left:
                max_diff = max(max_diff, nums[i] - left)
            else:
                left = min(left, nums[i])
        return max_diff

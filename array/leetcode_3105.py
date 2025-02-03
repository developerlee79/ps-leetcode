class Solution(object):
    def longestMonotonicSubarray(self, nums):
        n = len(nums)
        longest_len = 1
        increase = 1
        decrease = 1
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                longest_len = max(longest_len, increase, decrease)
                increase = 1
                decrease = 1
            elif nums[i] > nums[i - 1]:
                increase += 1
                longest_len = max(longest_len, decrease)
                decrease = 1
            else:
                decrease += 1
                longest_len = max(longest_len, increase)
                increase = 1
        return max(longest_len, increase, decrease)

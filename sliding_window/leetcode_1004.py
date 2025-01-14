class Solution(object):
    def longestOnes(self, nums, k):
        n = len(nums)
        i = 0
        j = 0
        zeros = k
        while j < n:
            zeros -= 1 - nums[j]
            if zeros < 0:
                zeros += 1 - nums[i]
                i += 1
            j += 1
        return j - i

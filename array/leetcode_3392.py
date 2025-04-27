class Solution(object):
    def countSubarrays(self, nums):
        n = len(nums)
        count = 0
        left = nums[0]
        mid = nums[1]
        for i in range(2, n):
            if (left + nums[i]) << 1 == mid:
                count += 1
            left = mid
            mid = nums[i]
        return count

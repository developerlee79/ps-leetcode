class Solution(object):
    def countAlternatingSubarrays(self, nums):
        n = len(nums)
        dp = [1] * n
        count = 0
        for i in range(n):
            if i != 0 and nums[i - 1] != nums[i]:
                dp[i] += dp[i - 1]
            count += dp[i]
        return count

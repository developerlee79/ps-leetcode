class Solution(object):
    def arrayNesting(self, nums):
        n = len(nums)
        dp = [-1] * n
        longest_len = 0
        for i in range(n):
            longest_len = max(longest_len, self.find_longest_len(nums, i, dp))
        return longest_len

    def find_longest_len(self, nums, i, dp):
        if dp[i] != -1:
            return dp[i]
        dp[i] = 0
        dp[i] += self.find_longest_len(nums, nums[i], dp) + 1
        return dp[i]

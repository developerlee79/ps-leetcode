class Solution(object):
    def canPartition(self, nums):
        sub_sum = sum(nums)

        if sub_sum % 2 != 0:
            return False

        sub_sum //= 2

        dp = [False] * (sub_sum + 1)
        dp[0] = True

        for num in nums:
            for curr_sum in range(sub_sum, num - 1, -1):
                dp[curr_sum] = dp[curr_sum] or dp[curr_sum - num]

        return dp[sub_sum]

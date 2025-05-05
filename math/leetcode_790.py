class Solution(object):
    def numTilings(self, n):
        if n < 3:
            return n
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] << 1) + dp[i - 3]
        return dp[-1] % (10**9 + 7)

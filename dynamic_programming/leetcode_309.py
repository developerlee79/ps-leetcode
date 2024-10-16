class Solution(object):
    def maxProfit(self, prices):
        dp = [-prices[0], 0, 0]
        n = len(prices)

        for i in range(1, n):
            price = prices[i]
            hold = dp[0]
            nothing = dp[1]
            cooldown = dp[2]
            dp[0] = max(hold, nothing - price)
            dp[1] = max(nothing, cooldown)
            dp[2] = hold + price

        return max(dp)

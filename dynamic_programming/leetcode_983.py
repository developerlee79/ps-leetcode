class Solution(object):
    def mincostTickets(self, days, costs):
        day_set = set(days)
        dp = [0] * 30

        for i in range(days[0], days[-1] + 1):
            if i in day_set:
                dp[i % 30] = min(
                    dp[(i - 1) % 30] + costs[0],
                    dp[max(0, i - 7) % 30] + costs[1],
                    dp[max(0, i - 30) % 30] + costs[2]
                )
            else:
                dp[i % 30] = dp[(i - 1) % 30]

        return dp[days[-1] % 30]

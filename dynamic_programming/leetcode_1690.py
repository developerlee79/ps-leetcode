class Solution(object):
    def stoneGameVII(self, stones):
        n = len(stones)
        totals = sum(stones)
        dp = [[-1] * (n + 1) for _ in range(n + 1)]
        return self.find_min_diff(stones, totals, 0, n - 1, dp)

    def find_min_diff(self, stones, totals, i, j, dp):
        if totals == 0 or i >= j:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        left_total = totals - stones[i]
        right_total = totals - stones[j]
        left = left_total - self.find_min_diff(stones, left_total, i + 1, j, dp)
        right = right_total - self.find_min_diff(stones, right_total, i, j - 1, dp)
        dp[i][j] = max(left, right)
        return dp[i][j]

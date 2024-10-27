class Solution(object):
    def countSquares(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        count = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    dp[i + 1][j + 1] = 1 + min(dp[i][j], dp[i + 1][j], dp[i][j + 1])
                    count += dp[i + 1][j + 1]

        return count

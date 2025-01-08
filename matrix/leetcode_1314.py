class Solution(object):
    def matrixBlockSum(self, mat, k):
        m = len(mat)
        n = len(mat[0])

        dp = [[0] * n for _ in range(m)]
        prefix_sum = 0

        for i, row in enumerate(mat):
            for j, col in enumerate(row):
                prefix_sum += col
                dp[i][j] = prefix_sum

        answer = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                answer[i][j] = dp[min(i + k, m - 1)][min(j + k, n - 1)]
                if i - k - 1 >= 0:
                    answer[i][j] -= dp[i - k - 1][-1]
                x = j + k
                y = j - k
                start = max(0, i - k)
                end = min(m, i + k + 1)
                for idx in range(start, end):
                    if idx < end - 1 and x + 1 < n:
                        answer[i][j] -= dp[idx][-1] - dp[idx][x]
                    if y > 0:
                        if idx > 0:
                            answer[i][j] -= dp[idx][y - 1] - dp[idx - 1][-1]
                        else:
                            answer[i][j] -= dp[idx][y - 1]

        return answer

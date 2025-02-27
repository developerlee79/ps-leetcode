class Solution(object):
    def lenLongestFibSubseq(self, arr):
        n = len(arr)
        index_map = {}
        dp = [[0] * n for _ in range(n)]
        answer = 0

        for i, num in enumerate(arr):
            index_map[num] = i

        for i in range(1, n):
            for j in range(i):
                target = arr[i] - arr[j]
                if target in index_map and index_map[target] < j:
                    dp[j][i] = dp[index_map[target]][j] + 1
                    answer = max(answer, dp[j][i])

        return answer + 2 if answer > 0 else 0

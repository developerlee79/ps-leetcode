class Solution(object):
    def canMakePaliQueries(self, s, queries):
        n = len(s) + 1
        counter = list(map(lambda ch: ord(ch) - 97, s))

        dp = [0] * n
        for i in range(1, n):
            dp[i] = dp[i - 1] ^ (1 << counter[i - 1])

        query_results = []

        for left, right, k in queries:
            count = bin(dp[left] ^ dp[right + 1]).count('1') >> 1
            query_results.append(count <= k)

        return query_results

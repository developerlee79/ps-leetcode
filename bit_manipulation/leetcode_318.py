class Solution(object):
    def maxProduct(self, words):
        n = len(words)
        dp = [0] * n

        for i, word in enumerate(words):
            for c in word:
                dp[i] |= 1 << ord(c) - 97

        max_product = 0

        for i, word in enumerate(words):
            m = len(word)
            for j in range(i + 1, n):
                if dp[i] & dp[j] > 0:
                    continue
                max_product = max(max_product, m * len(words[j]))

        return max_product

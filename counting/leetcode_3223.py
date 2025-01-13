class Solution(object):
    def minimumLength(self, s):
        dp = [0] * 26

        count = len(s)

        for ch in s:
            idx = ord(ch) - 97
            dp[idx] += 1
            if dp[idx] > 2:
                count -= 2
                dp[idx] = 1

        return count

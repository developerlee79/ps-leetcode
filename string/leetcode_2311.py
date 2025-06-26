class Solution(object):
    def longestSubsequence(self, s, k):
        n = len(s)
        bin_str = '{0:b}'.format(k)
        m = len(bin_str)
        if n < m:
            return n
        zeros = 0
        for i in range(n - m):
            if s[i] == '0':
                zeros += 1
        if bin_str >= s[n - m:]:
            return zeros + m
        else:
            return zeros + m - 1

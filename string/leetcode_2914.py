class Solution(object):
    def minChanges(self, s):
        n = len(s)

        count = 0

        for i in range(0, n - 1, 2):
            if s[i] != s[i + 1]:
                count += 1

        return count
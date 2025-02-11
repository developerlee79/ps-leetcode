class Solution(object):
    def countBinarySubstrings(self, s):
        n = len(s)
        count = 0
        pre = 0
        curr = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                count += min(curr, pre)
                pre = curr
                curr = 1
        return count + min(curr, pre)

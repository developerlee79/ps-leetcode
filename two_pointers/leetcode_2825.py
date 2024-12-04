class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        n = len(str1)
        m = len(str2)
        i = 0
        j = 0

        while i < n and j < m:
            if str1[i] == str2[j] or self.operation(str1[i]) == str2[j]:
                j += 1
            i += 1

        return j == m

    @staticmethod
    def operation(ch):
        if ch == 'z':
            return 'a'
        return chr(ord(ch) + 1)

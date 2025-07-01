class Solution(object):
    def possibleStringCount(self, word):
        n = len(word)
        count = 1
        i = 0
        while i < n:
            ch = word[i]
            i += 1
            while i < n and word[i] == ch:
                count += 1
                i += 1
        return count

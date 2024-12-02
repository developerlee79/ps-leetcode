class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        n = len(sentence)
        m = len(searchWord)
        i = 0
        idx = 1

        while i < n:
            j = 0
            while i < n and j < m and sentence[i] == searchWord[j]:
                i += 1
                j += 1
            if j == m:
                return idx
            while i < n and sentence[i] != ' ':
                i += 1
            i += 1
            idx += 1

        return -1

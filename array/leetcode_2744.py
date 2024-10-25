class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        n = len(words)

        max_pair = 0

        for i in range(n):
            for j in range(i + 1, n):
                if self.is_equal_in_reverse(words[i], words[j]):
                    max_pair += 1
                    break

        return max_pair

    @staticmethod
    def is_equal_in_reverse(word1, word2):
        if len(word1) != len(word2):
            return False

        i = 0
        j = len(word1) - 1

        while j >= 0:
            if word1[i] != word2[j]:
                return False
            i += 1
            j -= 1

        return True

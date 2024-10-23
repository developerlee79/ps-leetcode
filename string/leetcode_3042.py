class Solution(object):
    def countPrefixSuffixPairs(self, words):
        n = len(words)

        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                if self.is_prefix_and_suffix(words[i], words[j]):
                    count += 1

        return count

    @staticmethod
    def is_prefix_and_suffix(s1, s2):
        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        for k in range(n):
            if s1[k] != s2[k] or s1[-(k + 1)] != s2[-(k + 1)]:
                return False

        return True

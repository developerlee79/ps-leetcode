class Solution(object):
    def closetTarget(self, words, target, startIndex):
        n = len(words)
        i = startIndex
        j = startIndex
        count = 0

        while words[i] != target and words[j] != target:
            i -= 1
            if i < 0:
                i = n - 1
            j += 1
            if j >= n:
                j = 0
            if i == startIndex:
                return -1
            count += 1

        return count

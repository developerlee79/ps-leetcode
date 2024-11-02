class Solution(object):
    def makeFancyString(self, s):
        n = len(s)

        fancy_str = ""

        i = 0

        while i < n:
            count = 1
            j = i + 1
            while j < n and s[i] == s[j]:
                count += 1
                j += 1
            fancy_str += s[i] * min(count, 2)
            i = j

        return fancy_str

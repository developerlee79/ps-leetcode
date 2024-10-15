class Solution(object):
    def minimumSteps(self, s):
        count = 0

        i = len(s) - 1
        zero_count = 0

        while i >= 0:
            if s[i] == '0':
                zero_count += 1
            else:
                count += zero_count
            i -= 1

        return count

class Solution:
    def minOperations(self, s: str) -> int:
        zeros = 0
        ones = 0

        for i, ch in enumerate(s):
            if i & 1 == 0:
                if ch == '0':
                    ones += 1
                else:
                    zeros += 1
            else:
                if ch == '0':
                    zeros += 1
                else:
                    ones += 1

        return min(zeros, ones)

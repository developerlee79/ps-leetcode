class Solution(object):
    def minSteps(self, s, t):
        alphabets = [0] * 26

        for ch in s:
            alphabets[ord(ch) - 97] += 1

        steps = 0

        for ch in t:
            chr_idx = ord(ch) - 97
            alphabets[ord(ch) - 97] -= 1
            if alphabets[chr_idx] < 0:
                steps += 1

        return steps

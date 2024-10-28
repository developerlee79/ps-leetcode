class Solution(object):
    def longestNiceSubstring(self, s):
        n = len(s)

        if n < 2:
            return ""

        substring_set = set(s)

        for i, char in enumerate(s):
            if char.upper() in substring_set and char.lower() in substring_set:
                continue
            left = self.longestNiceSubstring(s[0:i])
            right = self.longestNiceSubstring(s[i + 1:])
            return left if len(left) >= len(right) else right

        return s

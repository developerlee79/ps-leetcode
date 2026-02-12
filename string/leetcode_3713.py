class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        longest = 0

        for i in range(n):
            counts = {}
            uniq_count = 0
            max_freq = 0

            for j in range(i, n):
                counts[s[j]] = counts.get(s[j], 0) + 1
                if counts[s[j]] == 1:
                    uniq_count += 1
                max_freq = max(max_freq, counts[s[j]])
                if max_freq * uniq_count == j - i + 1:
                    longest = max(longest, j - i + 1)

        return longest

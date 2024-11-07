class Solution(object):
    def largestCombination(self, candidates):
        max_bits = [0] * 24

        for candidate in candidates:
            i = candidate
            j = 0
            while i > 0:
                max_bits[j] += i & 1
                i >>= 1
                j += 1

        return max(max_bits)


candidates = [16, 17, 71, 62, 12, 24, 14]
print(Solution().largestCombination(candidates))

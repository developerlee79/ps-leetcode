class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        totals = 1 << k
        seen = set()

        for i in range(n - k + 1):
            seen.add(s[i: i + k])
            if len(seen) == totals:
                return True

        return len(seen) == totals

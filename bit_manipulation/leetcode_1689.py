class Solution:
    def minPartitions(self, n: str) -> int:
        count = 0
        for ch in n:
            count = max(count, int(ch))
        return count

class Solution(object):
    def differenceOfSums(self, n, m):
        total = n * (n + 1) / 2
        divisible = (n // m) * (m + (n // m) * m)
        return total - divisible

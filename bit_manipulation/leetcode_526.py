class Solution(object):
    def countArrangement(self, n):
        return self.count_permutations(n, 0, 1)

    def count_permutations(self, n, visited, idx):
        if visited == (1 << n) - 1:
            return 1

        count = 0
        for i in range(1, n + 1):
            if visited & (1 << i - 1) == 0 and self.is_divisible(i, idx):
                count += self.count_permutations(n, visited | (1 << i - 1), idx + 1)

        return count

    @staticmethod
    def is_divisible(a, b):
        return a % b == 0 or b % a == 0

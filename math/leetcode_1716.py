class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = int(n / 7)
        left = n % 7
        return 28 * weeks + 7 * self.find_sum(weeks - 1) + weeks * left + self.find_sum(left)

    @staticmethod
    def find_sum(n: int) -> int:
        return n * (n + 1) // 2

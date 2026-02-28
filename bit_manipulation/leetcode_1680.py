class Solution:
    def concatenatedBinary(self, n: int) -> int:
        total = 1

        for i in range(2, n + 1):
            total <<= i.bit_length()
            total = (total + i) % 1000000007

        return total

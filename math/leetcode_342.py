class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & n - 1 == 0 and self.count_trailing_zero_bits(n) % 2 == 0

    @staticmethod
    def count_trailing_zero_bits(x: int) -> int:
        return (x & -x).bit_length() - 1

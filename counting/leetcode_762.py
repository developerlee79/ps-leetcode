import math


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for num in range(left, right + 1):
            bit_count = self.bit_count(num)
            if self.is_prime(bit_count):
                count += 1
        return count

    @staticmethod
    def bit_count(n: int) -> int:
        count = 0
        while n:
            count += 1
            n &= n - 1
        return count

    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False

        return True

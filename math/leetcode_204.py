import math


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        num_set = set()
        num_set.add(1)

        for i in range(2, int(math.sqrt(n)) + 1):
            if i in num_set:
                continue
            for j in range(i << 1, n, i):
                num_set.add(j)

        return n - 1 - len(num_set)

import math


class Solution(object):
    def minOperations(self, k):
        operation = k - 1

        target = float(k)
        n = int(math.ceil(target / 2))

        for i in range(2, n + 1):
            operation = min(operation, (i - 1) + int(math.ceil(target / i)) - 1)

        return operation

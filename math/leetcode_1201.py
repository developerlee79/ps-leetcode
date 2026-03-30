import math


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def count_ugly(right: int) -> int:
            return ((right // a) + (right // b) + (right // c)
                    - (right // math.lcm(a, b)) - (right // math.lcm(b, c)) - right // math.lcm(a, c)
                    + (right // math.lcm(a, b, c)))

        low = 1
        high = n * min(a, b, c)
        result = high
        while low <= high:
            mid = (low + high) // 2
            if count_ugly(mid) >= n:
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result

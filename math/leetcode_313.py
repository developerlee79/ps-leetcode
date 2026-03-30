import heapq
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [0] * n
        ugly[0] = 1

        queue = [(prime, i, 0) for i, prime in enumerate(primes)]
        heapq.heapify(queue)

        for i in range(1, n):
            while queue[0][0] <= ugly[i - 1]:
                num, p_idx, u_idx = heapq.heappop(queue)
                heapq.heappush(queue, (primes[p_idx] * ugly[u_idx + 1], p_idx, u_idx + 1))

            num, p_idx, u_idx = heapq.heappop(queue)
            ugly[i] = num
            heapq.heappush(queue, (primes[p_idx] * ugly[u_idx + 1], p_idx, u_idx + 1))

        return ugly[-1]

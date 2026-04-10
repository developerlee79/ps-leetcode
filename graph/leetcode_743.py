from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance = [float('inf')] * (n + 1)
        distance[k] = 0

        for _ in range(n - 1):
            for u, v, w in times:
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

        max_time = max(distance[1:])
        return max_time if max_time != float('inf') else -1

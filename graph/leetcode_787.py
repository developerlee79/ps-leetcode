from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = {}

        for fr, to, price in flights:
            if fr not in dist:
                dist[fr] = []
            dist[fr].append((to, price))

        queue = [(src, 0, 0)]
        visited = {}
        while queue:
            node, curr, stop = queue.pop(0)
            if stop > k or node not in dist:
                continue
            for connect in dist[node]:
                next, cost = connect
                if next not in visited or curr + cost < visited[next] and stop <= k:
                    visited[next] = curr + cost
                    queue.append((next, curr + cost, stop + 1))
        
        return visited[dst] if dst in visited else -1

import heapq


class Solution(object):
    def maximumMinimumPath(self, grid):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n, m = len(grid), len(grid[0])

        heap = [(-grid[0][0], 0, 0)]
        visited = [[False] * m for _ in range(n)]

        while heap:
            value, x, y = heapq.heappop(heap)

            if x == n - 1 and y == m - 1:
                return -value

            for dx, dy in directions:
                next_x, next_y = x + dx, y + dy

                if not 0 <= next_x < n or not 0 <= next_y < m or visited[next_x][next_y]:
                    continue

                visited[next_x][next_y] = True
                heapq.heappush(heap, (max(value, -grid[next_x][next_y]), next_x, next_y))

        return -1

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        count = 0
        queue = []

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 1:
                    count += 1
                elif col == 2:
                    queue.append((i, j))
        
        times = 0
        visited = set()
        directions = [[1, 0], [-1 ,0], [0, 1], [0, -1]]
        while queue and count > 0:
            size = len(queue)
            for _ in range(size):
                x, y = queue.pop(0)
                for dir_x, dir_y in directions:
                    next_x = x + dir_x
                    next_y = y + dir_y
                    if not 0 <= next_x < m or not 0 <= next_y < n:
                        continue
                    if grid[next_x][next_y] != 1 or (next_x, next_y) in visited:
                        continue
                    count -= 1
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y))
            times += 1

        return times if count == 0 else -1

from typing import List


class Solution:

    DIRECTIONS = {
        1: [(0, -1), (0, 1)],
        2: [(1, 0), (-1, 0)],
        3: [(0, -1), (1, 0)],
        4: [(0, 1), (1, 0)],
        5: [(0, -1), (-1, 0)],
        6: [(0, 1), (-1, 0)],
    }

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        visited = {(0, 0)}
        queue = [(0, 0)]

        while queue:
            x, y = queue.pop(0)
            if x == m - 1 and y == n - 1:
                return True

            for dx, dy in self.DIRECTIONS[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    for dl, dr in self.DIRECTIONS[grid[nx][ny]]:
                        if nx + dl == x and ny + dr == y:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
                            break

        return False

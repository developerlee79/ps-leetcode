class Solution(object):

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def countUnguarded(self, m, n, guards, walls):
        grid = [[0] * n for _ in range(m)]

        for x, y in walls:
            grid[x][y] = 1

        for x, y in guards:
            grid[x][y] = 1

        for guard in guards:
            x, y = guard
            for direction in self.directions:
                i = x + direction[0]
                j = y + direction[1]
                while 0 <= i < m and 0 <= j < n and grid[i][j] != 1:
                    grid[i][j] = 2
                    i += direction[0]
                    j += direction[1]

        count = 0

        for row in grid:
            for col in row:
                if col == 0:
                    count += 1

        return count

class Solution(object):
    def countServers(self, grid):
        m = len(grid)
        n = len(grid[0])
        rows = [0] * m
        cols = [0] * n
        locations = []
        servers = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                rows[i] += col
                cols[j] += col
                if col == 1:
                    locations.append((i, j))
        for i, j in locations:
            if rows[i] > 1 or cols[j] > 1:
                servers += 1
        return servers

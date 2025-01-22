class Solution(object):

    directions = [
        [-1, 0],
        [0, -1],
        [0, 1],
        [1, 0],
    ]

    def highestPeak(self, is_water):
        m = len(is_water)
        n = len(is_water[0])
        height = [[-1] * n for _ in range(m)]
        queue = []
        for i, row in enumerate(is_water):
            for j, col in enumerate(row):
                if col == 1:
                    height[i][j] = 0
                    queue.append((i, j))
        while queue:
            i, j = queue.pop(0)
            for direction in self.directions:
                x, y = i + direction[0], j + direction[1]
                if 0 <= x < m and 0 <= y < n and height[x][y] == -1:
                    height[x][y] = height[i][j] + 1
                    queue.append((x, y))
        return height

class NeighborSum(object):

    adjacent_directions = [
        [-1 , 0],
        [0, -1],
        [0, 1],
        [1, 0]
    ]

    diagonal_directions = [
        [-1, -1],
        [-1, 1],
        [1, -1],
        [1, 1]
    ]

    def __init__(self, grid):
        n = len(grid)
        self.neighbor_sum = [[0] * 2 for _ in range(n ** 2)]
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                for x, y in self.adjacent_directions:
                    if 0 <= i + x < n and 0 <= j + y < n:
                        value = grid[i + x][j + y]
                        self.neighbor_sum[col][0] += value
                for x, y in self.diagonal_directions:
                    if 0 <= i + x < n and 0 <= j + y < n:
                        value = grid[i + x][j + y]
                        self.neighbor_sum[col][0] += value
                        self.neighbor_sum[col][1] += value

    def adjacentSum(self, value):
        return self.neighbor_sum[value][0] - self.neighbor_sum[value][1]

    def diagonalSum(self, value):
        return self.neighbor_sum[value][1]

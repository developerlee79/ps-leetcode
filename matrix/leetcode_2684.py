class Solution(object):

    moves = [
        [-1, 1],
        [0, 1],
        [1, 1]
    ]

    def maxMoves(self, grid):
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for _ in range(n)]

        max_move = -1

        for i, row in enumerate(grid):
            self.move_cells(grid, n, m, i, 0, dp)
            max_move = max(max_move, dp[i][0])

        return max_move

    def move_cells(self, grid, n, m, x, y, dp):
        if dp[x][y]:
            return dp[x][y]

        max_move = 0

        for move in self.moves:
            x_move, y_move = move
            x2 = x + x_move
            y2 = y + y_move

            if not 0 <= x2 < n or not 0 <= y2 < m or grid[x2][y2] <= grid[x][y]:
                continue

            max_move = max(max_move, self.move_cells(grid, n, m, x2, y2, dp) + 1)

        dp[x][y] = max_move
        return dp[x][y]

class Solution(object):
    def checkXMatrix(self, grid):
        n = len(grid)

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if i == j or i + j == n - 1:
                    if grid[i][j] == 0:
                        return False
                elif grid[i][j] != 0:
                    return False

        return True

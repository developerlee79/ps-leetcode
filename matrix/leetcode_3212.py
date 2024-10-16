class Solution(object):
    def numberOfSubmatrices(self, grid):
        n = len(grid)
        m = len(grid[0])

        self.convert_matrix(grid)

        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        has_x = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        count = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = grid[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
                has_x[i][j] = has_x[i - 1][j] or has_x[i][j - 1] or grid[i - 1][j - 1] == 1

                if dp[i][j] == 0 and has_x[i][j]:
                    count += 1

        return count

    def convert_matrix(self, matrix):
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                matrix[i][j] = self.convert_to_num(col)

    @staticmethod
    def convert_to_num(col):
        if col == 'X':
            return 1
        elif col == 'Y':
            return -1
        else:
            return 0

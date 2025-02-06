class Solution(object):
    def deleteGreatestValue(self, grid):
        answer = 0
        for row in grid:
            row.sort()
        m = len(grid)
        n = len(grid[0])
        last_idx = n - 1
        for _ in range(n):
            max_col = 0
            for i in range(m):
                max_col = max(max_col, grid[i][last_idx])
            last_idx -= 1
            answer += max_col
        return answer

class Solution(object):
    def gridGame(self, grid):
        n = len(grid[0])
        min_point = float('inf')
        top_sum = sum(grid[0])
        bottom_sum = 0
        for i in range(n):
            top_sum -= grid[0][i]
            min_point = min(min_point, max(top_sum, bottom_sum))
            bottom_sum += grid[1][i]
        return min_point

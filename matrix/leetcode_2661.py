class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        m = len(mat)
        n = len(mat[0])
        mat_location = {}
        for x, row in enumerate(mat):
            for y, col in enumerate(row):
                mat_location[col] = (x, y)
        rows = [m] * n
        cols = [n] * m
        for i, num in enumerate(arr):
            x, y = mat_location[num]
            rows[y] -= 1
            cols[x] -= 1
            if rows[y] == 0 or cols[x] == 0:
                return i
        return len(arr) - 1

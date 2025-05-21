class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        col = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row |= 1 << i
                    col |= 1 << j
        for i in range(m):
            for j in range(n):
                if row & (1 << i) != 0 or col & (1 << j) != 0:
                    matrix[i][j] = 0
        return matrix

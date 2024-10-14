class Solution(object):
    def modifiedMatrix(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        for i in range(m):
            max_value = -1

            for j in range(n):
                max_value = max(max_value, matrix[j][i])

            for j in range(n):
                if matrix[j][i] == -1:
                    matrix[j][i] = max_value

        return matrix

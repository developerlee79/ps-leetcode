from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        matrix_sum = 0
        min_element = float("inf")
        count = 0
        for row in matrix:
            for col in row:
                if col < 0:
                    count += 1
                matrix_sum += abs(col)
                min_element = min(min_element, abs(col))
        return matrix_sum if count & 1 == 0 else matrix_sum - (min_element << 1)

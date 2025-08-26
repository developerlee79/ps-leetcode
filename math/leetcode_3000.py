from math import sqrt
from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = 0
        max_diagonal = 0
        for i, dimension in enumerate(dimensions):
            x, y = dimension
            diagonal = self.cal_diagonal(x, y)
            area = x * y
            if diagonal > max_diagonal:
                max_diagonal = diagonal
                max_area = area
            elif diagonal == max_diagonal and area > max_area:
                max_area = area
        return max_area

    @staticmethod
    def cal_diagonal(x, y):
        return sqrt(x * x + y * y)

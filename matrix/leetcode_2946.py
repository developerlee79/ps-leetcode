from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat)
        m = len(mat[0])
        move = k if k < m else k % m

        for i in range(n):
            row = mat[i]
            for j, col in enumerate(row):
                idx = j + move
                if idx >= m:
                    idx -= m
                if col != row[idx]:
                    return False
            move = -move

        return True

from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        sorted_arr = []

        for row in grid:
            for col in row:
                sorted_arr.append(col)

        sorted_arr.sort()

        operations = 0
        mid = sorted_arr[len(sorted_arr) // 2]
        for num in sorted_arr:
            if (num - sorted_arr[0]) % x != 0:
                return -1
            operations += abs(num - mid) // x

        return operations

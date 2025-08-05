from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = len(fruits)
        for i, fruit in enumerate(fruits):
            for j, basket in enumerate(baskets):
                if fruit <= basket:
                    baskets[j] = 0
                    count -= 1
                    break
        return count

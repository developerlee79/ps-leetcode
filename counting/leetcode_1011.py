from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 0
        right = 0

        for weight in weights:
            left = max(left, weight)
            right += weight
        
        while left < right:
            mid = (left + right) >> 1
            day = 1
            curr = 0
            for weight in weights:
               if curr + weight > mid:
                   day += 1
                   curr = 0
               curr += weight
               if day > days:
                   break
            if day <= days:
                right = mid
            else:
                left = mid + 1
        
        return left

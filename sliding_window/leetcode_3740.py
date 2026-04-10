from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        
        num_map = {}
        min_dist = float('inf')

        for i, num in enumerate(nums):
            if num not in num_map:
                num_map[num] = [1]
            num_map[num].append(i)
            if len(num_map[num]) >= 4:
                min_dist = min(min_dist, (i - num_map[num][num_map[num][0]]) << 1)
                num_map[num][0] += 1
        
        return min_dist if min_dist != float('inf') else -1

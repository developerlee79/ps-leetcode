from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        
        dist = {}
        min_dist = float('inf')

        for i, num in enumerate(nums):
            if num not in dist:
                dist[num] = [1]
            dist[num].append(i)
            if len(dist[num]) >= 4:
                min_dist = min(min_dist, (i - dist[num][dist[num][0]] << 1))
                dist[num][0] += 1

        return min_dist if min_dist != float('inf') else -1

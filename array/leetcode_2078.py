from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dist = 0
        last_colors = {}

        for i, color in enumerate(colors):
            if color not in last_colors:
                last_colors[color] = i
            for last_color, last_index in last_colors.items():
                if last_color == color:
                    continue
                max_dist = max(max_dist, abs(i - last_index))

        return max_dist

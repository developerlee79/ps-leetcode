class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        curr, max_range, min_range = 0, 0, 0
        for diff in differences:
            curr += diff
            max_range = max(max_range, curr)
            min_range = min(min_range, curr)
        return max(0, (upper - max_range) - (lower - min_range) + 1)

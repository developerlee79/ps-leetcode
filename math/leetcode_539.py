class Solution(object):
    def findMinDifference(self, timePoints):
        clocks = []
        for time_point in timePoints:
            hour = int(time_point[0:2])
            minute = int(time_point[3:5])
            clocks.append(hour * 60 + 1440 + minute)
            clocks.append(hour * 60 + minute)
        clocks.sort()
        min_diff = 1440
        n = len(clocks)
        for i in range(1, n):
            min_diff = min(min_diff, clocks[i] - clocks[i - 1])
        return min_diff

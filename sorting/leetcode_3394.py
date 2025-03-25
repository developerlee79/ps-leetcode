class Solution(object):
    def checkValidCuts(self, n, rectangles):
        verticals = []
        horizontals = []

        for rectangle in rectangles:
            sx, sy, ex, ey = rectangle
            verticals.append([sx, ex])
            horizontals.append([sy, ey])

        vertical_cuts = self.merge(verticals)
        horizontal_cuts = self.merge(horizontals)

        return len(vertical_cuts) > 2 or len(horizontal_cuts) > 2

    @staticmethod
    def merge(intervals):
        intervals.sort()
        merged = []

        last = intervals[0]

        for interval in intervals[1:]:
            start, end = interval
            if start < last[1]:
                last[1] = max(last[1], end)
            else:
                merged.append(last)
                last = interval

        merged.append(last)

        return merged

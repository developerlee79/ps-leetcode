class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        merged = []

        last = intervals[0]

        for interval in intervals[1:]:
            start, end = interval
            if start <= last[1]:
                last[1] = max(last[1], end)
            else:
                merged.append(last)
                last = interval

        merged.append(last)

        return merged

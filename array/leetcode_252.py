class Solution(object):
    def canAttendMeetings(self, intervals):
        intervals.sort()

        last_end = 0
        for start, end in intervals:
            if start < last_end:
                return False
            last_end = end

        return True

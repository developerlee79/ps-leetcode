class Solution:
    def countDays(self, days, meetings):
        meetings.sort()

        count = 0
        curr_start = current_end = -1

        for start, end in meetings:
            if start > current_end:
                if current_end != -1:
                    count += current_end - curr_start + 1
                curr_start, current_end = start, end
            else:
                current_end = max(current_end, end)

        if current_end != -1:
            count += current_end - curr_start + 1

        return days - count

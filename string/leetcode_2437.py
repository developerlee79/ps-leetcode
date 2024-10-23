class Solution(object):
    def countTime(self, time):
        if time[4] == '?':
            count = 10
        else:
            count = 1

        if time[3] == '?':
            count *= 6

        if time[1] == '?':
            if time[0] == '0' or time[0] == '1':
                count *= 10
            elif time[0] == '2':
                count *= 4
            else:
                count *= 24

        if time[0] == '?':
            if time[1] != '?':
                if int(time[1]) > 3:
                    count *= 2
                else:
                    count *= 3

        return count

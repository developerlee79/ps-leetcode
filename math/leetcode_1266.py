class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        curX, curY = points[0]
        time = 0
        for point in points:
            abx = abs(curX - point[0])
            aby = abs(curY - point[1])
            time += min(abx, aby)
            time += abs(abx - aby)
            curX, curY = point
        return time

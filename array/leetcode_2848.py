class Solution(object):
    def numberOfPoints(self, nums):
        points = set([])
        count = 0

        for num in nums:
            start, end = num

            for i in range(start, end + 1):
                if i not in points:
                    count += 1
                points.add(i)

        return count

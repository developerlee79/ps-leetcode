import collections


class Solution(object):
    def findPairs(self, nums, k):
        counter = collections.Counter(nums)
        count = 0
        for num in counter:
            if k > 0:
                if num + k in counter:
                    count += 1
            elif counter[num] > 1:
                count += 1
        return count

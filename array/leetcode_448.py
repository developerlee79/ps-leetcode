import collections


class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums) + 1

        counter = collections.Counter(nums)
        disappeared_numbers = []

        for i in range(1, n):
            if counter.get(i) is None:
                disappeared_numbers.append(i)

        return disappeared_numbers

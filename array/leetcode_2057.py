class Solution(object):
    def smallestEqual(self, nums):
        for i, num in enumerate(nums):
            if i % 10 == num:
                return i
        return -1

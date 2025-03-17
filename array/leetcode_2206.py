from collections import Counter


class Solution(object):
    def divideArray(self, nums):
        pairs = len(nums) >> 1
        frequency = Counter(nums)
        count = 0
        for freq in frequency.values():
            count += freq >> 1
        return pairs <= count

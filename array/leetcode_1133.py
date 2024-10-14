import collections


class Solution(object):
    def largestUniqueNumber(self, nums):
        num_map = collections.Counter(nums)

        largest_num = -1

        for num in nums:
            if num_map[num] == 1:
                largest_num = max(largest_num, num)

        return largest_num

class Solution(object):
    def findMiddleIndex(self, nums):
        prefix_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            prefix_sum -= num

            if left_sum == prefix_sum:
                return i

            left_sum += num

        return -1

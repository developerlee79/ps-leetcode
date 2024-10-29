class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        n = len(nums)

        nums.sort()

        largest_sum = 0
        smallest_num = 101

        count = k

        i = 0

        while i < n and count > 0 > nums[i]:
            largest_sum += -nums[i]
            count -= 1
            smallest_num = min(smallest_num, -nums[i])
            i += 1

        while i < n:
            largest_sum += nums[i]
            smallest_num = min(smallest_num, nums[i])
            i += 1

        return largest_sum - (2 * smallest_num * (count % 2))

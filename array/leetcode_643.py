class Solution(object):
    def findMaxAverage(self, nums, k):
        current_sum = 0.0

        for i in range(k):
            current_sum += nums[i]

        max_average = current_sum / k

        n = len(nums)

        for i in range(k, n):
            current_sum -= nums[i - k]
            current_sum += nums[i]
            max_average = max(max_average, current_sum / k)

        return max_average

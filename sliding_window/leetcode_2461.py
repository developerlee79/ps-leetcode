class Solution(object):
    def maximumSubarraySum(self, nums, k):
        n = len(nums)
        elements = {}
        curr_sum = 0

        for i in range(k):
            curr_sum += nums[i]
            if nums[i] not in elements:
                elements[nums[i]] = 0
            elements[nums[i]] += 1

        max_sum = curr_sum if len(elements) == k else 0

        for i in range(k, n):
            curr_sum -= nums[i - k]
            elements[nums[i - k]] -= 1
            if elements[nums[i - k]] == 0:
                del elements[nums[i - k]]
            curr_sum += nums[i]
            if nums[i] not in elements:
                elements[nums[i]] = 0
            elements[nums[i]] += 1
            if len(elements) == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum

class Solution(object):
    def minimumSum(self, nums):
        min_sum = float('inf')
        n = len(nums)
        left = nums[0]
        right_min = [-1] * n
        for i in range(n - 2, -1, -1):
            if nums[right_min[i + 1]] < nums[i + 1]:
                right_min[i] = right_min[i + 1]
            else:
                right_min[i] = i + 1
        for i in range(1, n - 1):
            num = nums[i]
            right = nums[right_min[i]]
            if left < num and right < num:
                min_sum = min(min_sum, left + right + num)
            left = min(left, num)
        if min_sum == float('inf'):
            return -1
        return min_sum

class Solution(object):
    def maximumBeauty(self, nums, k):
        nums.sort()
        n = len(nums)
        max_len = 0
        j = 0
        k_range = k << 1

        for i, num in enumerate(nums):
            num_range = num - k_range
            while j < n and nums[j] < num_range:
                j += 1
            max_len = max(max_len, i - j + 1)

        return max_len

class Solution(object):
    def find_first_index(self, nums, target):
        n = len(nums)

        low, high = 0, n - 1

        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low

    def maximumCount(self, nums):
        return max(
            self.find_first_index(nums, 0),
            len(nums) - self.find_first_index(nums, 1)
        )

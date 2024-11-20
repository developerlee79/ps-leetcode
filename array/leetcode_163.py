class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        if not nums:
            return [[lower, upper]]

        n = len(nums)
        missing_ranges = []

        if lower != nums[0]:
            missing_ranges.append([lower, nums[0] - 1])

        for i in range(1, n):
            if nums[i - 1] + 1 != nums[i]:
                missing_ranges.append([nums[i - 1] + 1, nums[i] - 1])

        if upper != nums[-1]:
            missing_ranges.append([nums[-1] + 1, upper])

        return missing_ranges

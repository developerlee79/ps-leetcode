class Solution(object):
    def missingElement(self, nums, k):
        n = len(nums)

        missing_count = k

        for i in range(0, n - 1):
            diff = nums[i + 1] - nums[i] - 1
            if diff >= missing_count:
                return nums[i] + missing_count
            missing_count -= diff

        return nums[-1] + missing_count

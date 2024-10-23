class Solution(object):
    def isConsecutive(self, nums):
        nums.sort()

        n = len(nums)

        low = nums[0]
        high = low + len(nums) - 1

        for i in range(1, n):
            if nums[i] > high or nums[i] - 1 != nums[i - 1]:
                return False

        return True

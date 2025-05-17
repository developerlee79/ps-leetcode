class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        left, right = 0, n - 1
        mid = 0

        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1

class Solution(object):
    def thirdMax(self, nums):
        n = len(nums)
        nums.sort()
        num_set = set()
        for i in range(n - 1, -1, -1):
            num_set.add(nums[i])
            if len(num_set) > 2:
                return nums[i]
        return nums[-1]

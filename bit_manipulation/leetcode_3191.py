class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        operations = 0
        for i in range(0, n - 2):
            if nums[i] == 0:
                operations += 1
                self.flip_array(nums, i)
        for num in nums:
            if num == 0:
                return -1
        return operations

    @staticmethod
    def flip_array(nums, i):
        for i in range(i, i + 3):
            nums[i] = nums[i] ^ 1

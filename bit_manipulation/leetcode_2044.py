class Solution(object):

    count = 0

    def countMaxOrSubsets(self, nums):
        n = len(nums)
        max_value = 0

        for num in nums:
            max_value = max_value | num

        self.count_subsets(n, 0, 0, nums, max_value)

        return self.count

    def count_subsets(self, n, index, num, nums, max_value):
        if num == max_value:
            self.count += 1

        for i in range(index, n):
            self.count_subsets(n, i + 1, num | nums[i], nums, max_value)

class Solution(object):
    def subsetXORSum(self, nums):
        return self.get_subset_sum(nums, 0, 0)

    def get_subset_sum(self, nums, index, curr_sum):
        if index == len(nums):
            return curr_sum

        xor_subset = self.get_subset_sum(nums, index + 1, curr_sum ^ nums[index])
        subSet = self.get_subset_sum(nums, index + 1, curr_sum)

        return xor_subset + subSet

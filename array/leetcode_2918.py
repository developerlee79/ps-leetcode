class Solution(object):
    def minSum(self, nums1, nums2):
        zero_1, sum_1 = self.find_sum_and_zeros(nums1)
        zero_2, sum_2 = self.find_sum_and_zeros(nums2)
        if sum_1 > sum_2 and zero_2 == 0:
            return -1
        elif sum_1 < sum_2 and zero_1 == 0:
            return -1
        return max(sum_1, sum_2)

    @staticmethod
    def find_sum_and_zeros(nums):
        zero_count = 0
        sum_nums = 0
        for num in nums:
            if num == 0:
                zero_count += 1
                sum_nums += 1
            sum_nums += num
        return zero_count, sum_nums

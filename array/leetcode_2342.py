class Solution(object):
    def maximumSum(self, nums):
        max_sum = -1
        num_map = {}
        for num in nums:
            digit_sum = self.sum_of_digit(num)
            if digit_sum in num_map:
                max_sum = max(max_sum, num_map[digit_sum] + num)
                if num_map[digit_sum] < num:
                    num_map[digit_sum] = num
            else:
                num_map[digit_sum] = num
        return max_sum

    @staticmethod
    def sum_of_digit(num):
        count = 0
        for ch in str(num):
            count += int(ch)
        return count

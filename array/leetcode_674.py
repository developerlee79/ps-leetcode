class Solution(object):
    def findLengthOfLCIS(self, nums):
        longest_len = 0
        current_len = 0
        last_num = float('-inf')

        for num in nums:
            if num <= last_num:
                current_len = 1
            else:
                current_len += 1

            last_num = num
            longest_len = max(longest_len, current_len)

        return longest_len

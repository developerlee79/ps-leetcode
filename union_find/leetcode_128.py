class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0

        num_set = set(nums)

        longest_sequence = 1

        for num in nums:
            count = 1

            if num - 1 not in num_set:
                current_num = num + 1

                while current_num in num_set:
                    count += 1
                    current_num += 1

            longest_sequence = max(longest_sequence, count)

        return longest_sequence

class Solution(object):
    def longestSquareStreak(self, nums):
        num_set = set(nums)

        longest_streak = -1

        for num in nums:
            current_num = num
            streak = 0
            while current_num in num_set:
                streak += 1
                current_num *= current_num
            if streak > 1:
                longest_streak = max(longest_streak, streak)

        return longest_streak

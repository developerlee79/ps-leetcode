class Solution(object):
    def findFinalValue(self, nums, original):
        nums.sort()

        current_value = original

        for num in nums:
            if num == current_value:
                current_value *= 2

        return current_value

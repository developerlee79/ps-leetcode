class Solution(object):
    def findNumbers(self, nums):
        count = 0

        for num in nums:
            if len(str(num)) & 1 == 0:
                count += 1

        return count

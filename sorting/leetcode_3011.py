class Solution(object):
    def canSortArray(self, nums):
        n = len(nums)

        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    if self.count_bit(nums[j]) == self.count_bit(nums[j + 1]):
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]

        i = 1

        while i < n:
            if nums[i - 1] > nums[i]:
                return False
            i += 1

        return True

    @staticmethod
    def count_bit(num):
        i = num
        count = 0
        while i > 0:
            count += i & 1
            i >>= 1
        return count

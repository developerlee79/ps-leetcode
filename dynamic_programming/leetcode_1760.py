class Solution(object):
    def minimumSize(self, nums, maxOperations):
        left = 1
        right = max(nums)

        while left < right:
            mid = (left + right) >> 1
            count = 0
            for num in nums:
                count += (num - 1) // mid
            if count <= maxOperations:
                right = mid
            else:
                left = mid + 1

        return right

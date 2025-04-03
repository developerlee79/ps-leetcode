class Solution(object):
    def maximumTripletValue(self, nums):
        n = len(nums)
        triplet = 0

        suffix = [0] * n
        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], nums[i + 1])

        prefix = nums[0]
        for i in range(1, n - 1):
            triplet = max(triplet, (prefix - nums[i]) * suffix[i])
            prefix = max(prefix, nums[i])

        return triplet

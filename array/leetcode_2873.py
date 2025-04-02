class Solution(object):
    def maximumTripletValue(self, nums):
        n = len(nums)
        triplet = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                diff = nums[i] - nums[j]
                for k in range(j + 1, n):
                    triplet = max(triplet, diff * nums[k])

        return triplet

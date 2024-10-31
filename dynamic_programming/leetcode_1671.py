class Solution(object):
    def minimumMountainRemovals(self, nums):
        n = len(nums)

        increasing = [1] * n
        decreasing = [1] * n

        i = 0
        j = n - 1

        while i < n:
            for index in range(i):
                if nums[i] > nums[index]:
                    increasing[i] = max(increasing[i], increasing[index] + 1)
            for index in range(j + 1, n):
                if nums[j] > nums[index]:
                    decreasing[j] = max(decreasing[j], decreasing[index] + 1)
            i += 1
            j -= 1

        max_mountain = 0

        for i in range(n):
            if increasing[i] > 1 and decreasing[i] > 1:
                max_mountain = max(max_mountain, increasing[i] + decreasing[i] - 1)

        return n - max_mountain

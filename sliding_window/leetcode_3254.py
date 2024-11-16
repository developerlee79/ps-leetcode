class Solution(object):
    def resultsArray(self, nums, k):
        n = len(nums)
        powers = []

        for i in range(n - k + 1):
            power = nums[i]
            for j in range(i, i + k - 1):
                if nums[j] != nums[j + 1] - 1:
                    power = -1
                    break
                power = max(power, nums[j + 1])
            powers.append(power)

        return powers


nums = [1, 2, 3, 4, 3, 2, 5]
k = 3
print(Solution().resultsArray(nums, k))

class Solution(object):
    def minMaxGame(self, nums):
        n = len(nums)

        while n > 1:
            target = int(n / 2)
            for i in range(target):
                if i % 2 == 0:
                    nums[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    nums[i] = max(nums[2 * i], nums[2 * i + 1])
            n = target

        return nums[0]

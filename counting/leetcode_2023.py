class Solution(object):
    def numOfPairs(self, nums, target):
        n = len(nums)
        m = len(target)
        pairs = 0
        for i, num in enumerate(nums):
            num_len = len(num)
            for j in range(i + 1, n):
                if num_len + len(nums[j]) == m:
                    if num + nums[j] == target:
                        pairs += 1
                    if nums[j] + num == target:
                        pairs += 1
        return pairs

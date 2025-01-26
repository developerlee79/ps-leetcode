class Solution(object):
    def findLHS(self, nums):
        nums.sort()
        lhs = 0
        visited = {}
        for i, num in enumerate(nums):
            if num in visited:
                continue
            if num - 1 in visited:
                low = visited[num - 1]
            else:
                low = self.count_low(nums, num - 1, i - 1)
            high, same = self.count_high(nums, num, i + 1)
            visited[num] = same
            if low > 0 or high > 0:
                lhs = max(lhs, max(low, high) + same)
        return lhs

    @staticmethod
    def count_low(nums, target, idx):
        low = 0
        while idx >= 0 and nums[idx] == target:
            low += 1
            idx -= 1
        return low

    @staticmethod
    def count_high(nums, target, idx):
        n = len(nums)
        high = 0
        same = 1
        while idx < n and target + 1 >= nums[idx]:
            if target == nums[idx]:
                same += 1
            else:
                high += 1
            idx += 1
        return high, same

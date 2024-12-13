from heapq import heappush, heappop


class Solution(object):
    def findScore(self, nums):
        queue = []

        for i, num in enumerate(nums):
            heappush(queue, (num, i))

        score = 0

        while queue:
            x = heappop(queue)
            if nums[x[1]] == 0:
                continue
            else:
                score += nums[x[1]]
                nums[x[1]] = 0
                if x[1] > 0:
                    nums[x[1] - 1] = 0
                if x[1] < len(nums) - 1:
                    nums[x[1] + 1] = 0

        return score

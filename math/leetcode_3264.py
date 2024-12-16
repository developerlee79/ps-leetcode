import heapq


class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        queue = []
        heapq.heapify(queue)

        for i, num in enumerate(nums):
            heapq.heappush(queue, (num, i))

        for _ in range(k):
            num, i = heapq.heappop(queue)
            nums[i] *= multiplier
            heapq.heappush(queue, (nums[i], i))

        return nums

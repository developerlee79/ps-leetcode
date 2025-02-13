import heapq


class Solution(object):
    def minOperations(self, nums, k):
        queue = []
        heapq.heapify(queue)
        for num in nums:
            heapq.heappush(queue, num)
        count = 0
        while queue:
            x = heapq.heappop(queue)
            if x >= k or not queue:
                break
            y = heapq.heappop(queue)
            heapq.heappush(queue, (min(x, y) << 1) + max(x, y))
            count += 1
        return count

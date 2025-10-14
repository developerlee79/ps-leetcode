from typing import List
from heapq import heappush, heappop


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        queue = []
        max_subseq = {}
        for i, num in enumerate(nums):
            heappush(queue, (num, i))
            max_subseq[i] = num
        while len(queue) > k:
            num, i = heappop(queue)
            del max_subseq[i]
        return list(max_subseq.values())

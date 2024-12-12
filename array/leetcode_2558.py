class Solution(object):
    def pickGifts(self, gifts, k):
        queue = []
        heapq.heapify(queue)

        for gift in gifts:
            heapq.heappush(queue, -gift)

        for _ in range(k):
            gift = heapq.heappop(queue)
            heapq.heappush(queue, -int(math.sqrt(-gift)))

        return -sum(queue)

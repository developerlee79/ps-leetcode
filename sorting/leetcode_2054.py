import heapq

class Solution:
    def maxTwoEvents(self, events):
        events.sort(key=lambda x: x[0])

        min_heap = []
        max_event = 0
        current_max_event = 0

        for event in events:
            start, end, value = event

            while min_heap and min_heap[0][0] < start:
                current_max_event = max(current_max_event, heapq.heappop(min_heap)[1])

            max_event = max(max_event, current_max_event + value)
            heapq.heappush(min_heap, (end, value))

        return max_event

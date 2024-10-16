import heapq


class Solution(object):
    def longestDiverseString(self, a, b, c):
        heap = []

        if a > 0:
            heapq.heappush(heap, [-a, 'a'])
        if b > 0:
            heapq.heappush(heap, [-b, 'b'])
        if c > 0:
            heapq.heappush(heap, [-c, 'c'])

        happy_str = ""

        last_count = 0
        last_char = ''

        while len(heap) > 0:
            current_item = heapq.heappop(heap)

            if current_item[1] == last_char:
                if last_count == 2:
                    if len(heap) == 0:
                        break

                    next_item = heapq.heappop(heap)

                    happy_str += next_item[1]
                    next_item[0] += 1

                    last_char = next_item[1]
                    last_count = 1

                    if next_item[0] != 0:
                        heapq.heappush(heap, next_item)
                else:
                    happy_str += current_item[1]
                    current_item[0] += 1

                    last_count += 1
            else:
                happy_str += current_item[1]
                current_item[0] += 1

                last_char = current_item[1]
                last_count = 1

            if current_item[0] != 0:
                heapq.heappush(heap, current_item)

        return happy_str

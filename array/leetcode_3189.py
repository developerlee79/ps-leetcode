import heapq


class Solution(object):
    def minMoves(self, rooks):
        n = len(rooks)

        dp_row = [0] * n
        dp_col = [0] * n

        move_count = 0

        duplicates_row = []
        duplicates_col = []

        for rook in rooks:
            dp_row[rook[0]] += 1
            if dp_row[rook[0]] > 1:
                heapq.heappush(duplicates_row, rook[0])
            dp_col[rook[1]] += 1
            if dp_col[rook[1]] > 1:
                heapq.heappush(duplicates_col, rook[1])

        for i in range(n):
            if dp_row[i] == 0:
                move_count += abs(i - heapq.heappop(duplicates_row))
            if dp_col[i] == 0:
                move_count += abs(i - heapq.heappop(duplicates_col))

        return move_count

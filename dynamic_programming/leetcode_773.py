import copy
import heapq as hq


class Solution(object):
    class Board:
        def __init__(self, board, moves=0):
            self.x = None
            self.y = None
            self.board = board
            self.count = self.find_unsolved_tiles()
            self.moves = moves

        def __lt__(self, other):
            return self.count + self.moves < other.count + other.moves

        def is_solved(self):
            return self.count == 0

        def find_unsolved_tiles(self):
            count = 0
            number = 1
            for i in range(2):
                for j in range(3):
                    if self.board[i][j] == 0:
                        self.x = i
                        self.y = j
                    elif self.board[i][j] != number:
                        count += 1
                    number += 1
            return count

    directions = [
        [-1, 0], [1, 0], [0, -1], [0, 1]
    ]

    def slidingPuzzle(self, board):
        queue = [self.Board(board)]
        hq.heapify(queue)
        visited = {}

        while queue:
            curr_board = hq.heappop(queue)
            if curr_board.is_solved():
                return curr_board.moves
            for direction in self.directions:
                i, j = direction
                x = curr_board.x + i
                y = curr_board.y + j
                if not 0 <= x <= 1 or not 0 <= y <= 2:
                    continue
                if (x, y) in visited:
                    if curr_board.board in visited[(x, y)]:
                        continue
                else:
                    visited[(x, y)] = []
                visited[(x, y)].append(curr_board.board)
                new_board = self.move_puzzle(curr_board, direction)
                hq.heappush(queue, new_board)

        return -1

    def move_puzzle(self, old_board, direction):
        new_board = copy.deepcopy(old_board.board)
        i, j = direction
        new_board[old_board.x][old_board.y], new_board[old_board.x + i][old_board.y + j] \
            = new_board[old_board.x + i][old_board.y + j], new_board[old_board.x][old_board.y]
        return self.Board(new_board, old_board.moves + 1)

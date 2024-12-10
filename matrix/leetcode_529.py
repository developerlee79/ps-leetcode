class Solution(object):
    def updateBoard(self, board, click):
        m, n = len(board), len(board[0])
        x, y = click
        target = board[x][y]

        if target == 'M':
           board[x][y] = 'X'
        else:
            self.reveal_all_connected_empty(board, x, y, m, n)

        return board

    directions = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1]
    ]

    def has_adjacent_reveal(self, board, x, y, m, n):
        count = 0
        for next_x, next_y in self.directions:
            i, j = x + next_x, y + next_y
            if 0 <= i < m and 0 <= j < n:
                if board[i][j] == 'X' or board[i][j] == 'M':
                    count += 1
        return count

    def reveal_all_connected_empty(self, board, x, y, m, n):
        if board[x][y] != 'E':
            return

        count = self.has_adjacent_reveal(board, x, y, m, n)
        if count > 0:
            board[x][y] = str(count)
            return

        board[x][y] = 'B'

        for next_x, next_y in self.directions:
            i, j = x + next_x, y + next_y
            if 0 <= i < m and 0 <= j < n:
                self.reveal_all_connected_empty(board, i, j, m, n)

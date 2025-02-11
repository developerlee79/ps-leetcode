class Solution(object):
    move_map = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

    def judgeCircle(self, moves):
        x = 0
        y = 0
        for move in moves:
            moveX, moveY = self.move_map[move]
            x += moveX
            y += moveY
        return x == 0 and y == 0

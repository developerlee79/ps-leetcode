class Solution(object):

    directions = [
        [-1, 0],
        [0, -1],
        [1, 0],
        [0, 1]
    ]

    def isRobotBounded(self, instructions):
        location = [0, 0]
        idx = 0

        for _ in range(4):
            for instruction in instructions:
                if instruction == 'G':
                    x, y = self.directions[idx]
                    location[0] += x
                    location[1] += y
                elif instruction == 'L':
                    idx += 1
                    if idx > 3:
                        idx = 0
                else:
                    idx -= 1
                    if idx < 0:
                        idx = 3

        return location == [0, 0]

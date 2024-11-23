class Solution(object):
    def rotateTheBox(self, box):
        m, n = len(box), len(box[0])
        rotated = [['.'] * m for _ in range(n)]

        for i, row in enumerate(box):
            bottom = n - 1
            for j in range(n - 1, -1, -1):
                if row[j] == '#':
                    rotated[bottom][m - 1 - i] = '#'
                    bottom -= 1
                elif row[j] == '*':
                    rotated[j][m - 1 - i] = '*'
                    bottom = j - 1

        return rotated

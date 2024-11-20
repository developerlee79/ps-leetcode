class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        return self.is_black(coordinate1) == self.is_black(coordinate2)

    @staticmethod
    def is_black(coordinate):
        x = ord(coordinate[0]) - 96
        y = int(coordinate[1])
        return x & 1 == y & 1

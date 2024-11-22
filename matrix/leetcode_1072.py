class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        patterns = {}

        for row in matrix:
            if row[0] == 0:
                pattern = tuple(row)
            else:
                pattern = tuple(i ^ 1 for i in row)
            if pattern not in patterns:
                patterns[pattern] = 0
            patterns[pattern] += 1

        return max(patterns.values())

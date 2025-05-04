class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        count = 0
        domino_map = {}
        for i, j in dominoes:
            count += domino_map.get((i, j), 0)
            if i != j:
                count += domino_map.get((j, i), 0)
            domino_map[(i, j)] = domino_map.get((i, j), 0) + 1
        return count

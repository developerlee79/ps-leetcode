class Solution(object):
    def addSpaces(self, s, spaces):
        m = len(spaces)
        n = len(s) + m
        last_idx = 0
        space_idx = 0
        added_str = []

        for i in range(n):
            if space_idx < m and i == spaces[space_idx]:
                added_str.append(s[last_idx:i])
                last_idx = i
                space_idx += 1

        added_str.append(s[last_idx:])

        return " ".join(added_str)

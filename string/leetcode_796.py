class Solution(object):
    def rotateString(self, s, goal):
        n = len(s)

        if n != len(goal):
            return False

        idx = 0

        while idx < n:
            i = 0
            j = idx
            while i < n and s[i] == goal[j]:
                i += 1
                j += 1
                if j >= n:
                    j = 0
            if i == n:
                return True
            idx += 1

        return False

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)

        i = 0
        segment_exists = False
        while i < n:
            if s[i] == '1':
                if segment_exists:
                    return False
                while i < n and s[i] == '1':
                    i += 1
                segment_exists = True
            i += 1

        return True

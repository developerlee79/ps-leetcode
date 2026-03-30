class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        count_1 = [[0] * 26 for _ in range(2)]
        count_2 = [[0] * 26 for _ in range(2)]

        for i in range(n):
            count_1[i & 1][ord(s1[i]) - ord("a")] += 1
            count_2[i & 1][ord(s2[i]) - ord("a")] += 1
        for i in range(26):
            if count_1[0][i] != count_2[0][i] or count_1[1][i] != count_2[1][i]:
                return False

        return True

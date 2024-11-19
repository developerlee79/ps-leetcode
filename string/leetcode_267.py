import math
from collections import Counter


class Solution(object):
    def generatePalindromes(self, s):
        if len(s) == 1:
            return [s]

        counter = Counter(s)
        middle = ""

        for c in counter:
            if counter[c] & 1 == 1:
                if middle != "":
                    return []
                middle = c
                counter[c] -= 1
            counter[c] = math.ceil(counter[c] / 2)

        palindromes = []
        half_n = int(len(s) / 2)

        for c in counter:
            self.find_palindromes(counter, palindromes, c, c, half_n, middle)

        return palindromes

    def find_palindromes(self, counter, palindromes, target, half, n, middle):
        if counter[target] == 0:
            return
        if len(half) == n:
            palindromes.append(half + middle + half[::-1])
            return

        counter[target] -= 1
        for c in counter:
            self.find_palindromes(counter, palindromes, c, half + c, n, middle)
        counter[target] += 1

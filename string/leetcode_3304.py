class Solution(object):
    def kthCharacter(self, k):
        return chr(ord('a') + self.bit_count(k - 1))

    @staticmethod
    def bit_count(n):
        bits = 0
        while n:
            bits += 1
            n &= n - 1
        return bits

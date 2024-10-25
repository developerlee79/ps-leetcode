class Solution(object):
    def generateTheString(self, n):
        if n % 2 == 0:
            return 'a' * n
        return 'a' * (n - 1) + 'b'

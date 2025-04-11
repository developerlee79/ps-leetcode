class Solution(object):
    def countSymmetricIntegers(self, low, high):
        count = 0
        for i in range(low, high + 1):
            if self.is_symmetric(i):
                count += 1
        return count

    @staticmethod
    def is_symmetric(x):
        s = str(x)
        n = len(s)
        if n % 2 != 0:
            return False
        half = n // 2
        left = s[:half]
        right = s[half:]
        return sum(map(int, left)) == sum(map(int, right))

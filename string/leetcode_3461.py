class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        digits = []
        for c in s:
            digits.append(int(c))
        while n > 2:
            for i in range(n - 1):
                digits.append((digits.pop(0) + digits[0]) % 10)
            digits.pop(0)
            n -= 1
        return digits[0] == digits[1]

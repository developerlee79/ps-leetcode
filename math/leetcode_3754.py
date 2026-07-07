class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum_of_digits = 0
        x = 0
        m = str(n)
        for digit in m:
            if digit != '0':
                sum_of_digits += int(digit)
                x *= 10
                x += int(digit)
        return int(sum_of_digits * x)

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        big = max(num1, num2)
        small = min(num1, num2)
        while big != 0 and small != 0:
            count += int(big / small)
            tmp = small
            small = big % small
            big = tmp
        return count

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1] * n
        i = j = k = 0

        for idx in range(1, n):
            num1 = ugly[i] << 1
            num2 = ugly[j] * 3
            num3 = ugly[k] * 5

            min_num = min(num1, num2, num3)
            ugly[idx] = min_num

            if min_num == num1:
                i += 1
            if min_num == num2:
                j += 1
            if min_num == num3:
                k += 1

        return ugly[-1]

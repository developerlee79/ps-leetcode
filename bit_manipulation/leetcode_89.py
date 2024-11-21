class Solution(object):
    def grayCode(self, n):
        gray_codes = []
        m = 1 << n

        for i in range(m):
            gray_codes.append(i ^ (i >> 1))

        return gray_codes


n = 2
print(Solution().grayCode(n))

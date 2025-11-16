class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        ones = 0
        for i, ch in enumerate(s):
            if ch == '0':
                count += int(ones * (ones + 1) / 2)
                ones = 0
                continue
            ones += 1
        if ones > 0:
            count += int(ones * (ones + 1) / 2)
        return count % 1000000007

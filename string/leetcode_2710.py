class Solution(object):
    def removeTrailingZeros(self, num):
        index = len(num) - 1

        while index >= 0 and num[index] == '0':
            index -= 1

        return num[0:index + 1]

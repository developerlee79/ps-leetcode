class Solution(object):
    def getDescentPeriods(self, prices):
        n = len(prices)
        count = n
        smooth = 1

        for i in range(1, n):
            if prices[i - 1] - 1 == prices[i]:
                count += smooth
            else:
                smooth = 0
            smooth += 1

        return count

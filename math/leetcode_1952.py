class Solution(object):
    def isThree(self, n):
        if n < 4:
            return False

        count = 0

        for i in range(1, n / 2 + 1):
            if n % i == 0:
                count += 1
                if i != n / i:
                    count += 1
                if count > 3:
                    return False

        return count == 3

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        count = 0
        for i, num in enumerate(arr):
            if i > 2 and arr[i - 3] & 1 > 0:
                count -= 1
            if num & 1 > 0:
                count += 1
            if count == 3:
                return True
        return False

class Solution(object):
    def canThreePartsEqualSum(self, arr):
        total_sum = sum(arr)

        if total_sum % 3 != 0:
            return False

        part_sum = total_sum / 3

        i = 1
        j = len(arr) - 2

        left = arr[0]
        right = arr[-1]

        while i < j and left != part_sum:
            left += arr[i]
            i += 1

        while j > 0 and right != part_sum:
            right += arr[j]
            j -= 1

        if i > j:
            return False

        middle = 0

        for idx in range(i, j + 1):
            middle += arr[idx]

        return left == right == middle

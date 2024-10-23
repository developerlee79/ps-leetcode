class Solution(object):
    def missingNumber(self, arr):
        if arr[0] == arr[1]:
            return arr[0]

        n = len(arr)

        last_num = arr[0]

        for i in range(1, n - 1):
            left_diff = arr[i] - last_num
            right_diff = arr[i + 1] - arr[i]

            if abs(left_diff) > abs(right_diff):
                return arr[i] - right_diff
            elif abs(left_diff) < abs(right_diff):
                return arr[i] + left_diff

            last_num = arr[i]

        return -1

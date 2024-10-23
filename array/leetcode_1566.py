class Solution(object):
    def containsPattern(self, arr, m, k):
        n = len(arr)
        left = m * k

        for i in range(n - m + 1):
            if left > n - i:
                return False

            pattern = arr[i:i + m]

            is_break = False

            for j in range(2, k + 1):
                next_pattern = arr[i + m * (j - 1):i + m * j]
                if pattern != next_pattern:
                    is_break = True
                    break

            if is_break is not True:
                return True

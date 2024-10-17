class Solution(object):
    def maximumSwap(self, num):
        num_str = list(str(num))
        n = len(num_str)

        dp = []
        max_index = n - 1

        for i in range(n - 1, -1, -1):
            if num_str[i] > num_str[max_index]:
                max_index = i
            dp.append(max_index)

        dp.reverse()

        for i in range(n):
            if dp[i] != i and num_str[dp[i]] != num_str[i]:
                num_str[i], num_str[dp[i]] = num_str[dp[i]], num_str[i]
                break

        return int(''.join(num_str))

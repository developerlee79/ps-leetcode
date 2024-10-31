class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [nums[0]]

        for i in range(1, n):
            num = nums[i]
            if dp[-1] < num:
                dp.append(num)
            else:
                index = self.find_smallest_index(dp, num)
                dp[index] = num

        return len(dp)

    @staticmethod
    def find_smallest_index(dp, num):
        start, end = 0, len(dp) - 1

        while start < end:
            mid = start + end
            if dp[mid] == num:
                return mid
            elif dp[mid - 1] < num < dp[mid]:
                return mid
            elif num < dp[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return start

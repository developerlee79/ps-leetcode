class Solution(object):
    def maxCount(self, banned, n, maxSum):
        ban_set = set(banned)

        count = 0
        cur_sum = maxSum

        for i in range(1, n + 1):
            if i in ban_set:
                continue
            if cur_sum - i < 0:
                break
            cur_sum -= i
            count += 1

        return count

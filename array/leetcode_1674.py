class Solution(object):
    def minMoves(self, nums, limit):
        n = len(nums)
        prefix = [0] * ((limit << 1) + 2)

        for i in range(n >> 1):
            left, right = nums[i], nums[n - 1 - i]
            min_pair, max_pair = min(left, right), max(left, right)
            pair = left + right
            prefix[pair] -= 1
            prefix[pair + 1] += 1
            prefix[min_pair + 1] -= 1
            prefix[max_pair + limit + 1] += 1

        curr_move = min_move = n
        for i in range(2, (limit << 1) + 1):
            curr_move += prefix[i]
            min_move = min(min_move, curr_move)

        return min_move

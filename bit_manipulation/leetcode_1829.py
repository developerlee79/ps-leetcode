class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        n = len(nums)

        limit = 2 ** maximumBit - 1

        xor_result = nums[0]

        for i in range(1, n):
            xor_result ^= nums[i]

        answer = []

        for i in range(n):
            answer.append(xor_result ^ limit)
            xor_result ^= nums[n - 1 - i]

        return answer


nums = [0, 1, 1, 3]
maximumBit = 2

print(Solution().getMaximumXor(nums, maximumBit))

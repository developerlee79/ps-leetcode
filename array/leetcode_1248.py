class Solution(object):
    def numberOfSubarrays(self, nums, k):
        n = len(nums)

        counts = [0] * (n + 1)
        counts[0] = 1

        total = 0
        odds = 0

        for num in nums:
            odds += num & 1
            if odds >= k:
                total += counts[odds - k]
            counts[odds] += 1

        return total

class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        n = len(nums)
        indices = []
        last = 0
        for i, num in enumerate(nums):
            if num == key:
                start = max(last, i - k)
                last = min(i + k + 1, n)
                for j in range(start, last):
                    indices.append(j)
        return indices


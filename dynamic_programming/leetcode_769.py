class Solution(object):
    def maxChunksToSorted(self, arr):
        count = 0
        chunks = 0

        for i, num in enumerate(arr):
            chunks += num - i
            if chunks == 0:
                count += 1

        return count

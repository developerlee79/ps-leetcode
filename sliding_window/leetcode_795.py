class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        count = 0
        first = -1
        last = -1
        for i, num in enumerate(nums):
            if num <= right:
                if first == -1:
                    first = i
                if num >= left:
                    last = i
                    count += i - first + 1
                elif last != -1:
                    count += last - first + 1
            elif num > right:
                first = -1
                last = -1
        return count

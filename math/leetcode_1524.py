class Solution(object):
    def numOfSubarrays(self, arr):
        count = 0
        prefix = 0
        even = 0
        odd = 0

        for num in arr:
            prefix += num
            if prefix & 1 != 0:
                count += even + 1
                odd += 1
            else:
                count += odd
                even += 1

        return count % 1000000007

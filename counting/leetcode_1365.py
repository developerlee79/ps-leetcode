class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        left = 0

        for key in sorted(counter.keys()):
            temp = counter[key]
            counter[key] = left
            left += temp

        smaller = []

        for num in nums:
            smaller.append(counter[num])

        return smaller

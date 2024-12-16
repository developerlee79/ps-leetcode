class Solution(object):
    def minimalKSum(self, nums, k):
        nums.sort()

        total_sum = 0
        count = k
        last = -1

        for num in nums:
            if num != last and num <= count:
                count += 1
                total_sum += num
            last = num

        return ((count * (count + 1)) >> 1) - total_sum

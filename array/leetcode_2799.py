class Solution(object):
    def countCompleteSubarrays(self, nums):
        n = len(nums)
        count = 0

        num_set = set()
        num_bit = 0
        for num in nums:
            num_set.add(num)
            num_bit |= 1 << num

        k = len(num_set)

        for i in range(n - k + 1):
            check_bit = 0
            j = i
            while j < i + k:
                check_bit |= 1 << nums[j]
                j += 1
            if check_bit == num_bit:
                count += 1
            while j < n:
                check_bit |= 1 << nums[j]
                if check_bit == num_bit:
                    count += 1
                j += 1

        return count

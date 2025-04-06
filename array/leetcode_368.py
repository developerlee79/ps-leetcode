class Solution(object):
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        nums.sort()

        subsets = [1] * n
        last_elements = [-1] * n

        max_index = 0

        for i, num in enumerate(nums):
            for j in range(i):
                if num % nums[j] == 0 and subsets[i] < subsets[j] + 1:
                    subsets[i] = subsets[j] + 1
                    last_elements[i] = j
            if subsets[i] > subsets[max_index]:
                max_index = i

        divisible_subset = []

        while max_index != -1:
            divisible_subset.insert(0, nums[max_index])
            max_index = last_elements[max_index]

        return divisible_subset

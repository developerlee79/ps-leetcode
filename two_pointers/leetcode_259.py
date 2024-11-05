class Solution(object):
    def threeSumSmaller(self, nums, target):
        n = len(nums)

        nums.sort()

        count = 0

        for i in range(n - 2):
            j = i + 1
            k = n - 1

            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum < target:
                    count += k - j
                    j += 1
                else:
                    k -= 1

        return count

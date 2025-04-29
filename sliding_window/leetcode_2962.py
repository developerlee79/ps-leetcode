class Solution(object):
    def countSubarrays(self, nums, k):
        n = len(nums)
        count = 0
        max_num = max(nums)
        count_map = {}
        left = 0

        for i, num in enumerate(nums):
            count_map[num] = count_map.get(num, 0) + 1
            if count_map.get(max_num, 0) >= k:
                while left < n and count_map.get(max_num, 0) >= k:
                    count_map[nums[left]] -= 1
                    left += 1
            count += left

        return count

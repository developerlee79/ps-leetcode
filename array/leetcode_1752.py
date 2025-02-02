class Solution(object):
    def check(self, nums):
        n = len(nums)
        is_desc = False
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                if is_desc:
                    return False
                is_desc = True
        return True

class Solution(object):
    def minNumber(self, nums1, nums2):
        first_min = 9
        num_set = set()
        for num in nums1:
            first_min = min(first_min, num)
            num_set.add(num)

        second_min = 9
        nums2.sort()
        for num in nums2:
            if num in num_set:
                return num
            second_min = min(second_min, num)

        return min(first_min, second_min) * 10 + max(first_min, second_min)

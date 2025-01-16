class Solution(object):
    def xorAllNums(self, nums1, nums2):
        answer = 0
        if len(nums1) & 1 != 0:
            for num in nums2:
                answer ^= num
        if len(nums2) & 1 != 0:
            for num in nums1:
                answer ^= num
        return answer

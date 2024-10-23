class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        greater_elements = [-1] * len(nums1)

        index_map = {}

        for i, num in enumerate(nums2):
            index_map[num] = i

        n = len(nums2)

        for i, num in enumerate(nums1):
            target_index = index_map[num]
            for j in range(target_index, n):
                if nums2[j] > num:
                    greater_elements[i] = nums2[j]
                    break

        return greater_elements

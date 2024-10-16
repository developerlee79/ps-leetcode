class Solution(object):
    def anagramMappings(self, nums1, nums2):
        anagram_list = []

        for target in nums1:
            for i, num in enumerate(nums2):
                if target == num:
                    anagram_list.append(i)
                    nums2[i] = -1
                    break

        return anagram_list

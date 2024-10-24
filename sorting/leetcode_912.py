class Solution(object):
    def sortArray(self, nums):
        return self.merge_sort(nums, 0, len(nums) - 1)

    def merge_sort(self, arr, start, end):
        if start == end:
            return [arr[start]]

        half = (start + end) / 2

        arr1 = self.merge_sort(arr, start, half)
        arr2 = self.merge_sort(arr, half + 1, end)

        return self.merge(arr1, arr2)

    def merge(self, arr1, arr2):
        n = len(arr1)
        m = len(arr2)

        sorted_list = []

        i = 0
        j = 0

        while i < n and j < m:
            if arr1[i] < arr2[j]:
                sorted_list.append(arr1[i])
                i += 1
            else:
                sorted_list.append(arr2[j])
                j += 1

        while i < n:
            sorted_list.append(arr1[i])
            i += 1

        while j < m:
            sorted_list.append(arr2[j])
            j += 1

        return sorted_list

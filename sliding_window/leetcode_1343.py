class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        n = len(arr)
        i = 0
        slide_sum = 0

        while i < k:
            slide_sum += arr[i]
            i += 1

        count = 1 if slide_sum / k >= threshold else 0

        while i < n:
            slide_sum -= arr[i - k]
            slide_sum += arr[i]
            if slide_sum / k >= threshold:
                count += 1
            i += 1

        return count

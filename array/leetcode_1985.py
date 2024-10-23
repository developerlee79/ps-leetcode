class Solution(object):
    def kthLargestNumber(self, nums, k):
        num_lens = {}

        for num in nums:
            size = len(num)
            if size not in num_lens:
                num_lens[size] = []
            num_lens[size].append(int(num))

        left_count = k
        sorted_keys = sorted(num_lens.keys(), reverse=True)

        for key in sorted_keys:
            len_list_size = len(num_lens[key])
            if len_list_size >= left_count:
                return str(sorted(num_lens[key], reverse=True)[left_count - 1])
            left_count -= len_list_size

        return -1

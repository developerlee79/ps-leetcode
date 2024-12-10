from collections import Counter


class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        word_freq = []
        for word in words:
            word_freq.append(self.find_lex_smallest_count(word))

        word_freq.sort()

        counts = []
        for query in queries:
            curr_freq = self.find_lex_smallest_count(query)
            counts.append(self.count_smaller(word_freq, curr_freq))

        return counts

    @staticmethod
    def find_lex_smallest_count(word):
        freq_counter = Counter(word)
        for i in range(26):
            idx_chr = chr(i + 97)
            if idx_chr in freq_counter:
                return freq_counter[idx_chr]
        return 0

    @staticmethod
    def count_smaller(nums, target):
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = int((low + high) >> 1)
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1

        return n - low

class Solution(object):
    def countLargestGroup(self, n):
        freq = [0] * 37
        max_freq = 0
        for i in range(1, n + 1):
            sum_of_digits = self.sum_of_digits(i)
            freq[sum_of_digits] += 1
            max_freq = max(max_freq, freq[sum_of_digits])
        count = 0
        for fr in freq:
            if fr == max_freq:
                count += 1
        return count

    @staticmethod
    def sum_of_digits(i):
        count = 0
        int_str = str(i)
        for c in int_str:
            count += int(c)
        return count

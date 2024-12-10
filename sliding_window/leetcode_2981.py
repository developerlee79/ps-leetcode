class Solution(object):
    def maximumLength(self, s):
        n = len(s)
        max_len = -1

        start = 1
        end = n - 2

        while start <= end:
            window = int((start + end) / 2)
            counts = [0] * 26
            is_exist = False
            for i in range(n - window + 1):
                j = i + 1
                k = i + window
                while j < k:
                    if s[j] != s[j - 1]:
                        break
                    j += 1
                if j == k:
                    chr_idx = ord(s[i]) - 97
                    counts[chr_idx] += 1
                    if counts[chr_idx] > 2:
                        is_exist = True
                        break
            if is_exist:
                max_len = window
                start = window + 1
            else:
                end = window - 1

        return max_len

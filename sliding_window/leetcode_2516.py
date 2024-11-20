class Solution(object):
    def takeCharacters(self, s, k):
        if k == 0:
            return 0

        n = len(s)
        counter = [0] * 3
        correct = 0

        j = n - 1

        while j >= 0 and correct < 3:
            c_idx = ord(s[j]) - 97
            counter[c_idx] += 1
            if counter[c_idx] == k:
                correct += 1
            j -= 1

        if j == -1 and correct < 3:
            return -1

        j += 1

        count = n - j

        for i, c in enumerate(s):
            left_idx = ord(c) - 97
            counter[left_idx] += 1
            if counter[left_idx] == k:
                correct += 1

            while j < n and correct == 3:
                right_idx = ord(s[j]) - 97
                counter[right_idx] -= 1
                if counter[right_idx] < k:
                    correct -= 1
                j += 1
                if correct == 3:
                    count = min(count, i + n - j + 1)

        return count

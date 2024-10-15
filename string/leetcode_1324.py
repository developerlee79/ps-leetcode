class Solution(object):
    def printVertically(self, s):
        max_len = self.find_longest_word(s)

        vertical_words = [''] * max_len

        count = 0

        for char in s:
            if char == ' ':
                while count < max_len:
                    vertical_words[count] += ' '
                    count += 1
                count = 0
            else:
                vertical_words[count] += char
                count += 1

        for i, word in enumerate(vertical_words):
            vertical_words[i] = word.rstrip()

        return vertical_words

    @staticmethod
    def find_longest_word(s):
        max_len = 0
        curr_len = 0

        for char in s:
            if char == ' ':
                max_len = max(max_len, curr_len)
                curr_len = 0
            else:
                curr_len += 1

        return max(max_len, curr_len)

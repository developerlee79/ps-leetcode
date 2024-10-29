class Solution(object):
    def reorderSpaces(self, text):
        words = []
        spaces = 0

        curr_word = ''

        for c in text:
            if c == ' ':
                if curr_word != '':
                    words.append(curr_word)
                    curr_word = ''
                spaces += 1
            else:
                curr_word += c

        if curr_word != '':
            words.append(curr_word)

        n = len(words)
        splits = n - 1

        rearrange_text = words[0]

        for i in range(1, n):
            rearrange_text += (' ' * splits)
            spaces -= splits
            word = words[i]
            rearrange_text += word

        return rearrange_text + (' ' * spaces)

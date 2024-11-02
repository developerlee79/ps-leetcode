class Solution(object):
    def isCircularSentence(self, sentence):
        n = len(sentence)

        last_char = sentence[-1]

        i = 0

        while i < n:
            if last_char != sentence[i]:
                return False
            while i < n and sentence[i] != ' ':
                i += 1
            last_char = sentence[i - 1]
            i += 1

        return True

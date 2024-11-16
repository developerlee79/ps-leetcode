class Solution(object):
    def longestPalindrome(self, words):
        word_set = {}
        count = 0
        same_count = 0

        for word in words:
            if word not in word_set:
                word_set[word] = 0
            word_set[word] += 1

            reversed_word = word[::-1]
            if word == reversed_word:
                if word_set[word] > 1:
                    word_set[word] -= 2
                    count += 4
                    same_count -= 1
                else:
                    same_count += 1
            elif reversed_word in word_set and word_set[reversed_word] > 0:
                word_set[word] -= 1
                word_set[reversed_word] -= 1
                count += 4

        if same_count > 0:
            count += 2

        return count

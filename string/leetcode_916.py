from collections import Counter


class Solution(object):
    def wordSubsets(self, words1, words2):
        words_max_freq = self.word_max_frequency(words2)
        universals = []
        for word in words1:
            is_universal = True
            counter = Counter(word)
            for i, max_freq in enumerate(words_max_freq):
                if counter[chr(i + 97)] < max_freq:
                    is_universal = False
                    break
            if is_universal:
                universals.append(word)
        return universals

    @staticmethod
    def word_max_frequency(words):
        word_freq = [0] * 26
        for word in words:
            curr_freq = [0] * 26
            for c in word:
                curr_freq[ord(c) - 97] += 1
            for i in range(26):
                word_freq[i] = max(word_freq[i], curr_freq[i])
        return word_freq

class Solution(object):
    def findWordsContaining(self, words, x):
        answer = []
        for i, word in enumerate(words):
            if x in word:
                answer.append(i)
        return answer

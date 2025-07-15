vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}


class Solution:
    def isValid(self, word: str) -> bool:
        vowel = 0
        consonant = 0
        if len(word) < 3:
            return False
        for ch in word:
            if not ch.isalnum():
                return False
            if ch.isalpha():
                if ch in vowels:
                    vowel += 1
                else:
                    consonant += 1
        return vowel > 0 and consonant > 0

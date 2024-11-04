class Solution(object):
    def compressedString(self, word):
        n = len(word)
        i = 0

        compress_str = []

        while i < n:
            count = 1
            j = i + 1
            while j < n and word[i] == word[j] and count < 9:
                count += 1
                j += 1
            compress_str.append(str(count))
            compress_str.append(word[i])
            i = j

        return ''.join(compress_str)

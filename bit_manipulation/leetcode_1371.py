class Solution(object):
    vowel_set = {'a', 'e', 'i', 'o', 'u'}

    def findTheLongestSubstring(self, s):
        n = len(s)
        max_len = 0
        vowels = 0
        prefix_map = {0: -1}
        for i in range(n):
            if s[i] in self.vowel_set:
                vowel_bit = 1 << (ord(s[i]) - 97)
                vowels ^= vowel_bit
            if vowels in prefix_map:
                max_len = max(max_len, i - prefix_map[vowels])
            else:
                prefix_map[vowels] = i
        return max_len

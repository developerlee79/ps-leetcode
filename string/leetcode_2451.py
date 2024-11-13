class Solution(object):
    def oddString(self, words):
        m = len(words[0])

        diff_map = {}

        for word in words:
            diff = []
            for i in range(1, m):
                diff.append(str(ord(word[i]) - ord(word[i - 1])))
            diff_key = ",".join(diff)
            if diff_key not in diff_map:
                diff_map[diff_key] = []
            diff_map[diff_key].append(word)

        for diff, word_list in diff_map.items():
            if len(word_list) == 1:
                return word_list[0]

        return ""

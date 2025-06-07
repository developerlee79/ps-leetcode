class Solution(object):
    def clearStars(self, s):
        removes = set()
        char_map = {}
        for i, ch in enumerate(s):
            if ch == '*':
                for i in range(26):
                    target = chr(i + 97)
                    if target in char_map and char_map[target]:
                        removes.add(char_map[target].pop())
                        break
            else:
                if ch not in char_map:
                    char_map[ch] = []
                char_map[ch].append(i)
        answer = []
        for i, ch in enumerate(s):
            if i not in removes and ch != '*':
                answer.append(ch)
        return ''.join(answer)

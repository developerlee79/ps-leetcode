class Solution(object):
    def robotWithString(self, s):
        n = len(s)
        paper = []
        stack = []
        last_index = 0
        for i in range(26):
            target = chr(i + 97)
            while stack and ord(stack[-1]) <= ord(target):
                paper.append(stack.pop())
            for j in range(last_index, n):
                if s[j] == target:
                    paper.append(s[j])
                    for k in range(last_index, j):
                        stack.append(s[k])
                    last_index = j + 1
        while stack:
            paper.append(stack.pop())
        return ''.join(paper)

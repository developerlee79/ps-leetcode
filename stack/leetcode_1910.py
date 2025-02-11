class Solution(object):
    def removeOccurrences(self, s, part):
        m = len(part)
        stack = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= m and ''.join(stack[-m:]) == part:
                for _ in range(m):
                    stack.pop()
        return ''.join(stack)

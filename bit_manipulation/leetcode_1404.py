class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        stack = list(s)

        while stack:
            num = stack.pop()
            if not stack:
                break
            if num == '1':
                while stack and stack[-1] == '1':
                    stack.pop()
                    steps += 1
                if not stack:
                    stack.append('1')
                    steps += 1
                elif stack[-1] == '0':
                    stack.pop()
                    stack.append('1')
                    steps += 1
            steps += 1

        return steps

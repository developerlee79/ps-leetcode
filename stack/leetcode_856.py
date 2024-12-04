class Solution(object):
    def scoreOfParentheses(self, s):
        score = 0
        stack = []
        for c in s:
            if c == '(':
                stack.append(score)
                score = 0
            else:
                last__score = stack.pop()
                score = last__score + max(1, 2 * score)
        return score

class Solution(object):
    def checkValidString(self, s):
        lefts = []
        asterisks = []

        for i, ch in enumerate(s):
            if ch == '(':
                lefts.append(i)
            elif ch == ')':
                if not lefts:
                    if not asterisks:
                        return False
                    asterisks.pop(0)
                else:
                    lefts.pop()
            else:
                asterisks.append(i)

        while lefts:
            if not asterisks or lefts.pop() > asterisks.pop():
                return False

        return True

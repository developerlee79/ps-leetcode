class Solution(object):
    def addStrings(self, num1, num2):
        m = len(num2)
        added = []
        stack = []
        for num in num1:
            stack.append(int(num))
        carry = 0
        for i in range(m - 1, -1, -1):
            curr = int(num2[i]) + carry
            if stack:
                curr += stack.pop()
            carry = int(curr / 10)
            added.append(str(curr % 10))
        while stack:
            curr = stack.pop() + carry
            carry = int(curr / 10)
            added.append(str(curr % 10))
        if carry != 0:
            added.append("1")
        added.reverse()
        return "".join(added)

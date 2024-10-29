class Solution(object):
    def reformat(self, s):
        letters = []
        digits = []

        for c in s:
            if c.isdigit():
                digits.append(c)
            else:
                letters.append(c)

        reformatted_str = ""

        n = len(letters)
        m = len(digits)

        if abs(n - m) > 1:
            return reformatted_str

        if n == m:
            while letters:
                reformatted_str += letters.pop()
                reformatted_str += digits.pop()
        elif n > m:
            while digits:
                reformatted_str += letters.pop()
                reformatted_str += digits.pop()
            reformatted_str += letters.pop()
        else:
            while letters:
                reformatted_str += digits.pop()
                reformatted_str += letters.pop()
            reformatted_str += digits.pop()

        return reformatted_str

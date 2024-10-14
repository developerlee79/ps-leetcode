class Solution(object):
    def stringShift(self, s, shift):
        for command in shift:
            if command[0] == 0:
                s = self.shift_str(s, -command[1])
            else:
                s = self.shift_str(s, command[1])

        return s

    def shift_str(self, s, count):
        return s[-count:] + s[:-count]

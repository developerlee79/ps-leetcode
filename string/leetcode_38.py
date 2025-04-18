class Solution(object):
    def countAndSay(self, n):
        say = "1"
        for i in range(1, n):
            say = self.get_say(say)
        return say

    @staticmethod
    def get_say(say):
        n = len(say)
        curr_say = []

        curr_ch = say[0]
        count = 1

        for i in range(1, n):
            if curr_ch == say[i]:
                count += 1
            else:
                curr_say.append(str(count))
                curr_say.append(curr_ch)
                curr_ch = say[i]
                count = 1

        curr_say.append(str(count))
        curr_say.append(curr_ch)

        return ''.join(curr_say)

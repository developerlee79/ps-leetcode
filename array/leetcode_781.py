class Solution(object):
    def numRabbits(self, answers):
        colors = {}

        count = 0

        for answer in answers:
            if answer == 0:
                count += 1
                continue

            if answer not in colors:
                colors[answer] = 0
            colors[answer] += 1

            if colors[answer] == answer + 1:
                count += answer + 1
                del colors[answer]

        return count + sum(colors.keys()) + len(colors.keys())

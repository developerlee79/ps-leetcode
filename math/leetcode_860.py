class Solution(object):
    def lemonadeChange(self, bills):
        changes = [0] * 3

        for bill in bills:
            if bill == 5:
                changes[0] += 1
            elif bill == 10:
                if changes[0] == 0:
                    return False
                changes[0] -= 1
                changes[1] += 1
            else:
                if changes[0] == 0:
                    return False
                if changes[1] == 0:
                    if changes[0] < 3:
                        return False
                    changes[0] -= 3
                else:
                    changes[0] -= 1
                    changes[1] -= 1
                changes[2] += 1

        return True

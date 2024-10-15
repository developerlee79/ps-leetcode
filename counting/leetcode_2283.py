class Solution(object):
    def digitCount(self, num):
        counter = {}

        for i, digit in enumerate(num):
            counter[digit] = counter.get(digit, 0) + 1

            if counter.get(str(i)) is None:
                counter[str(i)] = 0

        for i, digit in enumerate(num):
            if counter[str(i)] != int(digit):
                return False

        return True

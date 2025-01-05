class Solution(object):
    def shiftingLetters(self, s, shifts):
        n = len(s)
        letters = list(s)
        range_sum = [0] * (n + 1)

        for start, end, direction in shifts:
            added = 1 if direction == 1 else -1
            range_sum[start] += added
            range_sum[end + 1] -= added

        prefix = 0
        for i in range(n):
            prefix += range_sum[i]
            letters[i] = chr(97 + self.find_letter_index(letters[i], prefix))

        return "".join(letters)

    @staticmethod
    def find_letter_index(letter, prefix):
        shift_count = (ord(letter) - 97 + prefix) % 26
        if shift_count < 0:
            shift_count += 26
        return shift_count

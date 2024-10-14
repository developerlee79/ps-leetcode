class Solution(object):
    def binaryGap(self, n):
        binary_str = "{0:b}".format(n)

        max_gap = 0
        last_bit = -1

        for i, binary in enumerate(binary_str):
            if binary == '1':
                if last_bit != -1:
                    max_gap = max(max_gap, i - last_bit)
                last_bit = i

        return max_gap

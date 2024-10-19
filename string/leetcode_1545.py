class Solution(object):
    def findKthBit(self, n, k):
        bit_string = "0"

        for _ in range(1, n):
            curr_len = len(bit_string)
            flipped = ""

            for i in range(curr_len - 1, -1, -1):
                flipped += '1' if bit_string[i] == '0' else '0'

            bit_string += '1' + flipped

        return bit_string[k - 1]

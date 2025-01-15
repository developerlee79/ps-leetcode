class Solution(object):
    def minimizeXor(self, num1, num2):
        left_bit = self.bit_count(num1)
        right_bit = self.bit_count(num2)

        if left_bit == right_bit:
            return num1
        elif left_bit < right_bit:
            return self.calculate_min_and_left(num1, right_bit - left_bit)
        else:
            return self.calculate_optimal(num1, right_bit)

    @staticmethod
    def bit_count(num):
        count = 0
        while num > 0:
            count += num & 1
            num >>= 1
        return count

    @staticmethod
    def calculate_min_and_left(num1, bit_count):
        x = num1
        location = 0
        while bit_count > 0 and (1 << location) < num1:
            if num1 & (1 << location) == 0:
                x |= 1 << location
                bit_count -= 1
            location += 1
        while bit_count > 0:
            x <<= 1
            x += 1
            bit_count -= 1
        return x

    @staticmethod
    def calculate_optimal(num1, bit_count):
        x = 0
        top_bit = 29
        for _ in range(bit_count):
            while num1 & (1 << top_bit) == 0:
                top_bit -= 1
            x |= 1 << top_bit
            top_bit -= 1
        return x

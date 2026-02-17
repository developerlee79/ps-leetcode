from typing import List


class Solution:
    def readBinaryWatch(self, num_leds: int) -> List[str]:
        if num_leds == 0:
            return ['0:00']

        valid_times = []
        MINUTE_MASK = 0b111111
        current_bits = (1 << num_leds) - 1
        max_limit = current_bits << (10 - num_leds)

        while current_bits <= max_limit:
            minutes = current_bits & MINUTE_MASK
            hours = current_bits >> 6

            if hours < 12 and minutes < 60:
                valid_times.append(f'{hours}:{minutes:0>2}')

            lowest_bit = current_bits & -current_bits
            higher_bits = current_bits + lowest_bit
            current_bits = (((current_bits ^ higher_bits) // lowest_bit) >> 2) | higher_bits

        return valid_times

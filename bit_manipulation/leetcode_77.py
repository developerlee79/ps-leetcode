from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr_comb = (1 << k) - 1
        max_limit = 1 << n

        combinations = []
        while curr_comb < max_limit:
            comb_list = []
            for i in range(n):
                if (curr_comb >> i) & 1:
                    comb_list.append(i + 1)
            combinations.append(comb_list)

            lowest_bit = curr_comb & -curr_comb
            highest_bit = curr_comb + lowest_bit
            curr_comb = highest_bit | ((curr_comb ^ highest_bit) // lowest_bit >> 2)

        return combinations

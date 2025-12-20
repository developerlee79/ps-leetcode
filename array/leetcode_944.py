from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        counting_array = [''] * len(strs[0])

        for s in strs:
            for j, char in enumerate(s):
                if counting_array[j] == 'A':
                    continue
                if counting_array[j] > char:
                    count += 1
                    counting_array[j] = 'A'
                else:
                    counting_array[j] = char

        return count

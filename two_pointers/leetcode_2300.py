from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(potions)
        potions.sort()
        success_spells = [0] * len(spells)
        for i, spell in enumerate(spells):
            success_spells[i] = n - self.get_highest_point(spell, success, potions)
        return success_spells

    @staticmethod
    def get_highest_point(spell: int, success: int, potions: List[int]) -> int:
        low = 0
        high = len(potions) - 1
        while low <= high:
            mid = int((high - low) / 2 + low)
            curr_point = spell * potions[mid]
            if curr_point >= success:
                high = mid - 1
            else:
                low = mid + 1
        return low

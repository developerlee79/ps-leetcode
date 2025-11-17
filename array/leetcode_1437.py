from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = k
        for num in nums:
            if num == 0:
                count += 1
            else:
                if count < k:
                    return False
                count = 0
        return True

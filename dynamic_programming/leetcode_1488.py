from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans: List[int] = [0] * n
        dry_days = []
        lakes = {}

        for i, rain in enumerate(rains):
            if rain == 0:
                dry_days.append(i)
            else:
                if rain in lakes:
                    is_dried = False
                    for dry in dry_days:
                        if dry > lakes[rain]:
                            ans[dry] = rain
                            dry_days.remove(dry)
                            is_dried = True
                            break
                    if not is_dried:
                        return []
                lakes[rain] = i
                ans[i] = -1

        for dry in dry_days:
            ans[dry] = 1

        return ans

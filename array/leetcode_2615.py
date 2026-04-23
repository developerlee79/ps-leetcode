from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * n

        dist = {}
        for i, num in enumerate(nums):
            if num not in dist:
                dist[num] = [0, i]
            else:
                dist[num][0] += i - dist[num][1]
                dist[num].append(i)

        for idxs in dist.values():
            left = 1
            right = len(idxs) - 2
            l_sum = 0
            r_sum = idxs[0]
            arr[idxs[1]] = idxs[0]
            for i in range(2, len(idxs)):
                diff = idxs[i] - idxs[i - 1]
                l_sum += diff * left
                r_sum -= diff * right
                arr[idxs[i]] = l_sum + r_sum
                left += 1
                right -= 1

        return arr

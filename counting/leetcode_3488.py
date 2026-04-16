from typing import List


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        num_map = {}
        answer = []

        for i, num in enumerate(nums):
            if num not in num_map:
                num_map[num] = []
            num_map[num].append(i)

        for query in queries:
            num = nums[query]
            indices = num_map[num]
            m = len(indices)

            if m == 1:
                answer.append(-1)
                continue

            left = 0
            right = m - 1
            pos = -1
            while left <= right:
                mid = (left + right) // 2
                if indices[mid] == query:
                    pos = mid
                    break
                elif indices[mid] < query:
                    left = mid + 1
                else:
                    right = mid - 1

            prev_idx = indices[(pos - 1) % m]
            next_idx = indices[(pos + 1) % m]

            def get_circular_dist(i, j, n):
                diff = abs(i - j)
                return min(diff, n - diff)

            res = min(
                get_circular_dist(query, prev_idx, n),
                get_circular_dist(query, next_idx, n),
            )
            answer.append(res)

        return answer

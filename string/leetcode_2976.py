from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(original)
        cost_map = [[float('inf')] * 26 for _ in range(26)]
        original_set = 0

        for i in range(n):
            ori_idx = ord(original[i]) - 97
            changed_idx = ord(changed[i]) - 97
            cost_map[ori_idx][changed_idx] = min(
                cost_map[ori_idx][changed_idx],
                cost[i]
            )
            original_set |= 1 << ori_idx

        for k in range(26):
            if original_set & (1 << k) == 0:
                continue
            for i in range(26):
                if original_set & (1 << i) == 0:
                    continue
                for j in range(26):
                    cost_map[i][j] = min(cost_map[i][j], cost_map[i][k] + cost_map[k][j])

        m = len(source)
        total_cost = 0

        for i in range(m):
            if source[i] == target[i]:
                continue
            operation_cost = cost_map[ord(source[i]) - 97][ord(target[i]) - 97]
            if operation_cost == float("inf"):
                return -1
            total_cost += operation_cost

        return total_cost

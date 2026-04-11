from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = []
        for i in range(26):
            count.append([0, float('-inf')])

        for task in tasks:
            count[ord(task) - 65][0] += 1

        jobs = len(tasks)
        time = 0
        
        while jobs > 0:
            min_idx = -1
            for i in range(26):
                if count[i][0] > 0 and time - count[i][1] > n:
                    if min_idx == -1 or count[min_idx][0] < count[i][0]:
                        min_idx = i
            if min_idx != -1:
                count[min_idx][0] -= 1
                count[min_idx][1] = time
                jobs -= 1
            time += 1

        return time

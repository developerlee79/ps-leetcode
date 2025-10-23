from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total_importance = 0

        connects = {}
        for employee in employees:
            connects[employee.id] = employee

        queue = [connects[id]]
        while queue:
            employee = queue.pop(0)
            total_importance += employee.importance
            for subordinate in employee.subordinates:
                queue.append(connects[subordinate])
            connects[employee.id] = []

        return total_importance

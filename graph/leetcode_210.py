from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_map = {}
        in_degree = [0] * numCourses

        for course, pre in prerequisites:
            if pre not in course_map:
                course_map[pre] = []
            course_map[pre].append(course)
            in_degree[course] += 1

        course_order = []
        queue = []

        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.pop(0)
            course_order.append(node)
            if node not in course_map:
                continue
            for next in course_map[node]:
                in_degree[next] -= 1
                if in_degree[next] == 0:
                    queue.append(next)

        return course_order if len(course_order) == numCourses else []

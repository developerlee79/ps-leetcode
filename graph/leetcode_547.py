class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        graph = {}

        for i, row in enumerate(isConnected):
            for j, col in enumerate(row):
                if i == j:
                    continue
                if col == 1:
                    if i not in graph:
                        graph[i] = set()
                    graph[i].add(j)

        count = n - len(graph)

        for i in range(n):
            if i in graph:
                self.remove_connection(graph, i, set())
                count += 1

        return count

    def remove_connection(self, graph, i, visited):
        if i not in graph or i in visited:
            return

        visited.add(i)

        for city in graph[i]:
            self.remove_connection(graph, city, visited)

        del (graph[i])

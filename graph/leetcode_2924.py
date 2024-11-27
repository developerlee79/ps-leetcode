class Solution(object):
    def findChampion(self, n, edges):
        if not edges:
            return 0 if n < 2 else -1

        team_graph = {}

        for a, b in edges:
            if a not in team_graph:
                team_graph[a] = []
            team_graph[a].append(b)

        for i in range(n):
            if self.is_champion(team_graph, i, n, set()):
                return i

        return -1

    def is_champion(self, team_graph, i, n, visited):
        if i in visited or i not in team_graph:
            return len(visited) == n

        visited.add(i)

        for weaker in team_graph[i]:
            if self.is_champion(team_graph, weaker, n, visited):
                return True
            visited.add(weaker)

        return len(visited) == n

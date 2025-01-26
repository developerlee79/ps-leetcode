class Solution(object):
    def eventualSafeNodes(self, graph):
        n = len(graph)
        dp = [0] * n
        safe_nodes = []
        for i in range(n):
            if self.is_safe(graph, dp, i):
                safe_nodes.append(i)
        return safe_nodes

    def is_safe(self, graph, dp, idx):
        if dp[idx] != 0:
            return dp[idx] == 1
        dp[idx] = 2
        for i in graph[idx]:
            if not self.is_safe(graph, dp, i):
                return False
        dp[idx] = 1
        return True

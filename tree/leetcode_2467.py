class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
        n = len(amount)
        graph = self.construct_graph(edges)
        parents = [-1] * n
        self.find_parent(graph, parents, -1, 0)
        time_stamp = self.find_bob_timestamp(parents, bob)
        return self.find_max_profit(graph, time_stamp, amount, 0, -1, 0)

    @staticmethod
    def construct_graph(edges):
        graph = {}
        for a, b in edges:
            if a not in graph:
                graph[a] = []
            graph[a].append(b)
            if b not in graph:
                graph[b] = []
            graph[b].append(a)
        return graph

    def find_parent(self, graph, parents, parent, node):
        parents[node] = parent
        for child in graph[node]:
            if parent == child:
                continue
            self.find_parent(graph, parents, node, child)

    @staticmethod
    def find_bob_timestamp(parents, bob):
        time_stamp = [-1] * len(parents)
        time = 0
        while bob != -1:
            time_stamp[bob] = time
            bob = parents[bob]
            time += 1
        return time_stamp

    def find_max_profit(self, graph, time_stamp, amount, node, parent, time):
        profit = 0
        if time_stamp[node] == -1 or time < time_stamp[node]:
            profit = amount[node]
        elif time == time_stamp[node]:
            profit = amount[node] >> 1
        is_leaf = True
        max_profit = float('-inf')
        for next_node in graph[node]:
            if parent == next_node:
                continue
            is_leaf = False
            max_profit = max(
                max_profit,
                self.find_max_profit(graph, time_stamp, amount, next_node, node, time + 1)
            )
        if not is_leaf:
            profit += max_profit
        return profit

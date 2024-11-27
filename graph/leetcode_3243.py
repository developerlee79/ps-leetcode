class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        dest_distances = [i for i in range(n - 1, -1, -1)]
        connects = [[] for _ in range(n)]

        for i in range(n - 1):
            connects[i + 1].append(i)

        distances = []

        for u, v in queries:
            connects[v].append(u)
            dest_distances[u] = min(dest_distances[u], dest_distances[v] + 1)
            self.find_shortest_distance(connects, u, dest_distances)
            distances.append(dest_distances[0])

        return distances

    def find_shortest_distance(self, connects, node, dest):
        for connect_node in connects[node]:
            if dest[connect_node] <= dest[node]:
                continue
            dest[connect_node] = dest[node] + 1
            self.find_shortest_distance(connects, connect_node, dest)

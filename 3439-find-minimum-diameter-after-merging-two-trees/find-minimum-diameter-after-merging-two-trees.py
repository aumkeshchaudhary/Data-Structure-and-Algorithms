class Solution(object):
    def minimumDiameterAfterMerge(self, edges1, edges2):
        from collections import defaultdict, deque

        def tree_diameter(edges, n):
            def bfs(node):
                dist = [-1] * n
                dist[node] = 0
                queue = deque([node])
                farthest_node = node
                max_dist = 0
                while queue:
                    curr = queue.popleft()
                    for neighbor in graph[curr]:
                        if dist[neighbor] == -1:
                            dist[neighbor] = dist[curr] + 1
                            queue.append(neighbor)
                            if dist[neighbor] > max_dist:
                                max_dist = dist[neighbor]
                                farthest_node = neighbor
                return farthest_node, max_dist

            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            
            farthest_node, _ = bfs(0)

            _, diameter = bfs(farthest_node)
            return diameter

        n = len(edges1) + 1
        m = len(edges2) + 1

        diameter1 = tree_diameter(edges1, n)
        diameter2 = tree_diameter(edges2, m)

        min_diameter = max(diameter1, diameter2, (diameter1 + 1) // 2 + (diameter2 + 1) // 2 + 1)
        return min_diameter

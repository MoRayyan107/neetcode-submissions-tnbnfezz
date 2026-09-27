class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def dsf_recursive(visited, start, graph):
            visited[start] = True

            for neighbour in graph[start]:
                if not visited[neighbour]:
                    dsf_recursive(visited,neighbour,graph)

        graph = defaultdict(list)
        count = 0
        visited = [False] * n

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        for i in range(n):
            if not visited[i]:
                count += 1
                dsf_recursive(visited, i, graph)

        return count
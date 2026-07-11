class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # print(graph)

        visited = set()
        res = 0
        for node in range(n):
            if node not in visited:
                q = deque([node])
                vertices = 0 # count number of nodes in a subgraph
                edges = 0 # number of edges

                while q:
                    cur = q.popleft()
                    if cur in visited:
                        continue
                    visited.add(cur)
                    vertices += 1
                    for nei in graph[cur]:
                        if nei not in visited:
                            edges += 1
                            q.append(nei)
                
                if vertices*(vertices-1)//2 == edges:
                    res += 1
        return res
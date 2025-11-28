class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.ans = 0
        def dfs(root, parent):
            s = values[root]
            for child in graph[root]:
                if child != parent:
                    s += dfs(child, root)
            if s%k == 0:
                self.ans += 1
                return 0
            return s

        dfs(0, -1)
        return self.ans
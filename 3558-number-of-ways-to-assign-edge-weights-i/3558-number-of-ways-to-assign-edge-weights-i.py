from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:

        def dfs(g, cur, prt):
            mx = 0

            for nxt in g[cur]:
                if nxt == prt:
                    continue

                mx = max(mx, dfs(g, nxt, cur) + 1)

            return mx

        n = len(edges) + 1

        g = [[] for _ in range(n + 1)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        mx = dfs(g, 1, 0)

        return pow(2, mx - 1, 10**9 + 7)
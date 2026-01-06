class Solution:
    def dfs(self, node, values, visited, tree, k):
        visited[node] = True
        total = values[node]

        for connected_node in tree[node]:
            if not visited[connected_node]:
                total += self.dfs(connected_node, values, visited, tree, k)

        if total % k == 0:
            self.ans += 1
            return 0
        return total

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        self.ans = 0
        visited = [False] * n
        tree = defaultdict(list)

        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        self.dfs(0, values, visited, tree, k)
        return self.ans
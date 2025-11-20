class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf, g, off, ans = list(range(c+1)), defaultdict(list), set(), []
        def find(x):
            if uf[x]!=x:
                uf[x] = find(uf[x])
            return uf[x]
        for x, y in connections:
            uf[find(y)] = find(x)
        for i, x in enumerate(uf):
            heappush(g[find(x)], i)
        for i, x in queries:
            if i==2:
                off.add(x)
                while g[find(x)] and g[find(x)][0] in off:
                    heappop(g[find(x)])
                continue
            a = -1
            if x not in off:
                a = x
            elif g[find(x)]:
                a = g[find(x)][0]
            ans.append(a)
        return ans
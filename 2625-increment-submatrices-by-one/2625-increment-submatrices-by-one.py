class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            r2 += 1; c2 += 1;
            res[r1][c1] += 1
            if c2 < n:
                res[r1][c2] -= 1
            if r2 < n:
                res[r2][c1] -= 1
                if c2 < n:
                    res[r2][c2] += 1
        
        delta = [0] * n
        for i, row in enumerate(res):
            acc = 0
            for j, x in enumerate(row):
                delta[j] += x
                acc += delta[j]
                res[i][j] = acc 

        return res
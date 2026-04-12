class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a,b):
            if a == 26 or b == 26:
                return 0
            return abs(a//6-b//6) + abs(a%6-b%6)
        n = len(word)
        A = ord('A')
        idx = [ord(c)-A for c in word]
        dp = [[float('inf')]*27 for _ in range(27)]
        dp[26][26] = 0
        for c in idx:
            ndp = [[float('inf')]*27 for _ in range(27)]
            for i in range(27):
                for j in range(27):
                    v = dp[i][j]
                    if v >= float('inf'):
                        continue
                    if v+dist(i,c) < ndp[c][j]:
                        ndp[c][j] = v + dist(i,c)
                    if v+dist(j,c) < ndp[i][c]:
                        ndp[i][c] = v + dist(j,c)
            dp = ndp
        return min(min(row) for row in dp)
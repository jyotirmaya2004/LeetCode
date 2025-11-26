class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        M = len(grid)
        N = len(grid[0])
        dp = [[[-1] * k for _ in range(N)] for _ in range(M)]
        def solve(i, j, curr):
            if i >= M or j >= N:
                return 0
            curr = ( curr + grid[i][j]) % k
            if i == M - 1 and j == N - 1:
                if curr == 0:
                    return 1
                return 0
            if dp[i][j][curr] != -1:
                return dp[i][j][curr]

            down = solve( i + 1, j, curr)
            right = solve( i, j + 1, curr)

            dp[i][j][curr] = (down + right) % (10 ** 9 + 7)
            return dp[i][j][curr]
        
        return solve(0, 0, 0)
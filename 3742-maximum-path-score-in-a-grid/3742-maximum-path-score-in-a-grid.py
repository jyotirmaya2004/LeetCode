from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        mxc = min(k + 1, n + m + 5)
        dp = [[[-1] * mxc for _ in range(m)] for _ in range(n)]
        dp[0][0][0] = 0

        for i in range(n):
            for j in range(m):
                for c in range(mxc):
                    if dp[i][j][c] == -1:
                        continue
                    # move right
                    if j + 1 < m:
                        cost = c + (1 if grid[i][j + 1] > 0 else 0)
                        if cost < mxc:
                            dp[i][j + 1][cost] = max(dp[i][j + 1][cost],
                                                      dp[i][j][c] + grid[i][j + 1])
                    # move down
                    if i + 1 < n:
                        cost = c + (1 if grid[i + 1][j] > 0 else 0)
                        if cost < mxc:
                            dp[i + 1][j][cost] = max(dp[i + 1][j][cost],
                                                      dp[i][j][c] + grid[i + 1][j])
        
        return max(dp[n-1][m-1])
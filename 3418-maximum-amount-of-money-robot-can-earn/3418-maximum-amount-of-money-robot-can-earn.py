class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])

        dp = [[-inf] * 3 for _ in range(n+1)]
        # initialise the first row
        dp[1] = [0] * 3

        for i in range(m):
            for j in range(n):
                x = coins[i][j]
                up0, up1, up2 = dp[j+1]
                left0, left1, left2 = dp[j]
                dp[j+1][0] = max(up0, left0) + x
                dp[j+1][1] = max(up1+x, left1+x, up0, left0) 
                dp[j+1][2] = max(up2+x, left2+x, up1, left1) 

        return dp[n][2]

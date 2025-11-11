class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp=[[0]*(n+1) for _ in range(m+1)]
        for s in strs:
            zeroes,ones=s.count('0'),s.count('1')
            for x in range(m,-1,-1):
                for y in range(n,-1,-1):
                    if zeroes<=x and ones<=y:
                        dp[x][y]=max(dp[x][y],dp[x-zeroes][y-ones]+1)
        return dp[-1][-1]